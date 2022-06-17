from battle import *
from deck import *
from dice import *

class CoreBase:
    # Default max stat points available for all creature creation
    maxPossibleStatPoints = 30
    
    def __init__(self):
        self.players = []
        self.warlords = []
        self.gladiator = None
        deckSize = 50
        self.deck = create_creature_deck(deckSize, self.maxPossibleStatPoints, shuffle = True)
        self._uidIndex = deckSize

    def tick_modifiers(self):
        for creature in itertools.chain(p.creatures for p in self.players):
            for modifier in creature.modifiers:
                modifier.numTurns -= 1
                if modifier.numTurns <= 0:
                    creature.remove_modifier(modifier)

    def create_warlords(self):
        self.warlords = [Warlord(2) for _ in range(3)]
        for w in self.warlords:
            w.creatures.extend(
                    create_creature(1, self.maxPossibleStatPoints, 0.02)
                    for _ in range(2)
                )
            w.creatures[0].baseDefense += 1
            w.creatures[1].baseAttack += 1
        print('Warlords created')
        for w in self.warlords:
            for c in w.creatures:
                c.uid = self._uidIndex
                self._uidIndex += 1
                print(c)
        print('\n')
    
    def create_gladiator(self):
        self.gladiator = Gladiator(3)
        for _ in range(3):
            creature = create_creature(2, self.maxPossibleStatPoints, 0.25)
            creature.uid = self._uidIndex
            self._uidIndex += 1
            self.gladiator.creatures.append(creature)
        self.gladiator.creatures[0].baseAttack += 1
        self.gladiator.creatures[1].baseDefense += 1
        self.gladiator.creatures[2].baseMaxHP += 5
        self.gladiator.creatures[2].heal()
        print('Gladiator created')
        for c in self.gladiator.creatures:
            print(c)