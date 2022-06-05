import itertools
import random


class TieredObjectBase:
    tiers = ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary')
    tieredVolumeThresholds = {0: 0.56, 1: 0.26, 2: 0.12, 3: 0.06, 4: 0.00}
    tierQualityThresholds = {
            0: [0.50, 0.56],
            1: [0.56, 0.63],
            2: [0.63, 0.70],
            3: [0.70, 0.80],
            4: [0.80, 1.00]
        }

    def __init__(self, *args, **kwargs):
        self.uid = None
        self.tier = None


class Creature(TieredObjectBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.baseAttack = 0
        self.baseDefense = 0
        self.baseHP = 1

    def __str__(self):
        return '\n'.join((
                f'Creature UID {self.uid}:',
                f'Tier:\t\t\t{self.tiers[self.tier]}',
                f'Base Attack:\t{self.baseAttack}',
                f'Base Defense:\t{self.baseDefense}',
                f'Base HP:\t\t{self.baseHP}'
            ))


class Deck(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __str__(self, *args, **kwargs):
        return '\n\n'.join(i.__str__() for i in self)

    def __add__(self, other):
        self += other
        return self

    def combine(self, *others, resetUID = True):
        self += itertools.chain(*others)
        if resetUID:
            uidCounter = 1
            for item in self:
                item.uid = uidCounter
                uidCounter += 1
        return self

    def shuffle(self):
        random.shuffle(self)
        return self


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
    newCreature.baseHP = round(remainingStatPoints * weight)
    remainingStatPoints -= newCreature.baseHP

    # Determine attack weighting
    newCreature.baseAttack = round(random.uniform(0.34, 0.67) * remainingStatPoints)

    # Give remaining points to defense
    newCreature.baseDefense = round(remainingStatPoints - newCreature.baseAttack)

    return newCreature


def create_deck_tiers(totalNumCards, maxPossibleStatPoints):
    # Calculate nubmer of cards per tier
    cardsPerTier = [
            int(round(Creature.tieredVolumeThresholds[i] * totalNumCards))
            for i in TieredObjectBase.tieredVolumeThresholds
        ]

    # Correct floating point or rounding errors by adding or removing common cards
    cardsPerTier[0] += totalNumCards - sum(cardsPerTier)

    weightVariance = 0.0
    for tier, tierNumCards in enumerate(cardsPerTier):
        # Allow more chaotic stat distribution per tier
        weightVariance += 0.035
        for i in range(tierNumCards):
            newCreature = create_creature(tier, maxPossibleStatPoints, weightVariance, uid = (tier + i))
            yield newCreature


def create_deck(totalNumCards):
    deck = Deck(c for c in create_deck_tiers(totalNumCards, 30))
    deck.shuffle()
    return deck


def main():
    deck = create_deck(50)
    print(deck)


main()
