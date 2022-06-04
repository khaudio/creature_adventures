import random
import statistics


class Deck(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __str__(self, *args, **kwargs):
        return ''.join(i.__str__() for i in self)

    def shuffle(self):
        random.shuffle(self)
        return self


class Creature:
    statTotalMinimums = (15, 17, 19, 21)
    statTotalMaximums = (17, 19, 21, 24)
    rarityStrs = ('Common', 'Uncommon', 'Rare', 'Epic')

    def __init__(self):
        self.uid = None
        self.rarity = 0
        self.baseAttack = 0
        self.baseDefense = 0
        self.baseHP = 1

    def stat_total_minimum(self):
        return self.statTotalMinimums[self.rarity]

    def stat_total_maximum(self):
        return self.statTotalMaximums[self.rarity]

    def stat_ratio(self):
        return (self.stat_total() / self.stat_total_maximum())

    def stat_total(self):
        return (self.baseAttack + self.baseDefense + self.baseHP)

    def rarity_str(self):
        return self.rarityStrs[self.rarity]

    def __str__(self):
        return f'''
        Creature UID {self.uid}:
        Rarity:\t\t\t{self.rarity_str()}
        Stat Ratio:\t\t{round(self.stat_ratio(), 2)}
        Stat Total:\t\t{self.stat_total()} / {self.stat_total_maximum()}
        Base Attack:\t{self.baseAttack}
        Base Defense:\t{self.baseDefense}
        Base HP:\t\t{self.baseHP}\n'''


def stat_generator(targetMean):
    return int(round(targetMean * random.lognormvariate(0.0, 0.173)))


def trim_stats(creature):
    '''Trim random stats until stats are within limits'''
    while True:
        statTotal = creature.stat_total()
        if (statTotal > creature.stat_total_maximum()):
            pick = random.randint(0, 2)
            if not pick and creature.baseAttack > 1:
                creature.baseAttack -= 1
            elif pick == 1 and creature.baseDefense:
                creature.baseDefense -= 1
            elif creature.baseHP > 5:
                creature.baseHP -= 1
        elif (statTotal < creature.stat_total_minimum()):
            pick = random.randint(0, 2)
            if not pick:
                creature.baseAttack += 1
            elif pick == 1:
                creature.baseDefense += 1
            else:
                creature.baseHP += 1
        else:
            break
    return creature


def create_sub_deck(numCreatures, targetMeanAtk, targetMeanDef, targetMeanHP, rarity):
    deck = Deck()

    for i in range(numCreatures):
        newCreature = Creature()

        newCreature.baseAttack = stat_generator(targetMeanAtk)
        newCreature.baseDefense = stat_generator(targetMeanDef)
        newCreature.baseHP = stat_generator(targetMeanHP)
        newCreature.rarity = rarity

        deck.append(trim_stats(newCreature))

    return deck


def combine_decks(*decks, shuffle = True):
    deck = Deck()

    uid = 1
    
    # Combine sub decks
    for d in decks:
        deck += d
    
    # Re-assign all UIDs to be unique
    for creature in deck:
        creature.uid = uid
        uid += 1
    
    # Shuffle the deck
    if shuffle:
        deck.shuffle()
    
    return deck


def main():
    # Create sub decks by rarity and combine

    # Normal creatures
    normalSubDeck = create_sub_deck(28, 3, 3, 10, 0)

    # Uncommon creatures
    uncommonSubDeck = create_sub_deck(13, 3.25, 3.25, 10.75, 1)

    # Rare creatures
    rareSubDeck = create_sub_deck(6, 3.75, 3.75, 11, 2)

    # Epic creatures
    epicSubDeck = create_sub_deck(3, 5.25, 5.25, 13.5, 3)

    deck = combine_decks(normalSubDeck, uncommonSubDeck, rareSubDeck, epicSubDeck, shuffle = False)

    print(deck)


main()

