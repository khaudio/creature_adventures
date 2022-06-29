import random
from creature import *
from item import *

class Deck(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __str__(self, *args, **kwargs):
        return '\n\n'.join(i.__str__() for i in self)

    @staticmethod
    def _sequence_uids(iterable, index = 1):
        for item in iterable:
            item.uid = index
            index += 1
        return iterable

    def __add__(self, other):
        merged = self + other
        return self._sequence_uids(merged)

    def reset_uids(self, index = 1):
        self = self._sequence_uids(self, index)
        return self

    def combine(self, *others, resetUID = True):
        for other in others:
            self += other
        if resetUID:
            self.reset_uids()
        return self

    def shuffle(self):
        random.shuffle(self)
        return self
    
    def draw(self):
        return self.pop()


def create_creature(tier, maxPossibleStatPoints, weightVariance, uid = None):
    newCreature = Creature()

    newCreature.tier = tier
    newCreature.uid = uid

    # Calculate total stat points available for this creature
    remainingStatPoints = random.uniform(
            Creature.tierQualityThresholds[tier][0],
            Creature.tierQualityThresholds[tier][1]
        ) * maxPossibleStatPoints

    # Determine how weighted towards HP stats will be distributed
    weight = random.uniform(0.45 - weightVariance, 0.75 + weightVariance)

    # Assign base HP value
    newCreature.baseMaxHP = round(remainingStatPoints * weight)
    newCreature.heal()
    remainingStatPoints -= newCreature.baseMaxHP

    # Determine attack weighting
    newCreature.baseAttack = round(random.uniform(0.54, 0.88) * remainingStatPoints)

    # Give remaining points to defense
    newCreature.baseDefense = round(remainingStatPoints - newCreature.baseAttack)

    return newCreature


def create_creature_deck(totalNumCards, maxPossibleStatPoints = 30):
    deck = Deck()

    # Calculate nubmer of cards per tier
    cardsPerTier = [
            int(round(Creature.tieredVolumeRatios[i] * totalNumCards))
            for i in Creature.tieredVolumeRatios
        ]

    # Correct floating point or rounding errors
    # by adding or removing common cards
    cardsPerTier[0] += int(totalNumCards - sum(cardsPerTier))

    weightVariance = 0.0
    for tier, tierNumCards in enumerate(cardsPerTier):
        # Allow more chaotic stat distribution per tier
        weightVariance += 0.035
        for _ in range(tierNumCards):
            newCreature = create_creature(
                    tier,
                    maxPossibleStatPoints,
                    weightVariance
                )
            deck.append(newCreature)

    # Deduplicate UIDs
    deck.reset_uids()

    return deck


def create_single_item_deck(itemClass, totalNumCards, maxPossibleValue):
    deck = Deck()

    # Calculate nubmer of cards per tier
    cardsPerTier = [
            int(round(Item.tieredVolumeRatios[i] * totalNumCards))
            for i in Item.tieredVolumeRatios
        ]
    
    # Correct floating point or rounding errors
    # by adding or removing common cards
    cardsPerTier[0] += int(totalNumCards - sum(cardsPerTier))

    for tier, tierNumCards in enumerate(cardsPerTier):
        for _ in range(tierNumCards):
            deck.append(itemClass(
                    tier,
                    maxPossibleValue,
                    persistent = False
                ))

    # Deduplicate UIDs
    deck.reset_uids()

    return deck


def create_item_deck(totalNumCards, maxPossibleStatPoints):
    # Use a portion for Potions and Elixirs
    chunk = round(totalNumCards * 0.6)
    chunk += (1 if chunk % 2 else 0)
    designatedSlice = int(chunk / 2)
    
    # Use remaining cards to create other items
    remainingSlice = round((totalNumCards - chunk) / 3)

    deck = Deck()
    
    deck += create_single_item_deck(Potion, designatedSlice, round(maxPossibleStatPoints / 3))
    deck += create_single_item_deck(Elixir, designatedSlice, round(maxPossibleStatPoints / 5))

    deck += create_single_item_deck(Poison, remainingSlice, -round(maxPossibleStatPoints / 3))
    deck += create_single_item_deck(Revive, remainingSlice, maxPossibleStatPoints)
    deck += create_single_item_deck(Net, remainingSlice, round(maxPossibleStatPoints) / 5)

    # Correct rounding errors by removing Potions
    while len(deck) > totalNumCards:
        deck.remove[0]

    # Deduplicate UIDs
    deck.reset_uids()
    
    return deck

