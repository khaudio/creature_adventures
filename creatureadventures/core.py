from battle import *
from deck import *
from dice import *

class CoreBase:
    # Default max stat points available for all creature creation
    maxPossibleStatPoints = 30
    globalActions = [Strike, Meditate, Brace, Dodge, Switch]
    
    def __init__(self):
        self.players = []
        self.warlords = []
        self.gladiator = None
        deckSize = 50
        self.creatureDeck = create_creature_deck(
                deckSize,
                self.maxPossibleStatPoints,
                shuffle = True
            )
        self._uidIndex = deckSize

    def draw(self):
        return self.creatureDeck.draw()

    def tick_modifiers(self):
        for p in self.players:
            for creature in p.creatures:
                for modifier in creature.modifiers:
                    modifier.numTurns -= 1
                    print(f'Modifier on UID {creature.uid} has {modifier.numTurns} remaining')
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

    def prompt_battle_action(self, battle, invoker, target):
        print(f'Choose action for creature {invoker.uid}...\nChoices:\n')
        choices = dict()
        for i, action in enumerate(self.globalActions):
            choices[i] = action(invoker, target)
        for action in invoker.availableActions:
            choices[len(choices)] = action(invoker, target)
        for i, action in choices.items():
            print(f'\t{i}:\t{action.name}')
        print('')
        if not choices:
            raise IndexError('No choices available!')
        try:
            choiceNumber = int(input())
        except:
            raise TypeError('Must be int')
        else:
            if not choiceNumber < len(choices):
                raise IndexError('User choice is out of range')
            return choices[choiceNumber]
    
    def run_battle(self, attackingCreature, defendingCreature, pvp):
        print(f'Creating {"pvp" if pvp else "pve"} battle...')
        battle = Battle(attackingCreature, defendingCreature, pvp)
        while battle.active():
            print('Cycling battle turn...')
            self.tick_modifiers()
            for creature in battle._participants:
                print(f'UID {creature.uid} has {len(creature.modifiers)} active modifiers')
            c1, c2 = battle._participants
            action = self.prompt_battle_action(battle, c1, c2)
            battle.stage_action(action)
            if battle.pvp:
                counterAction = self.prompt_battle_action(battle, c2, c1)
                battle.stage_action(counterAction)
            battle.run()
            # yield
        else:
            print('Battle is over')
            victor = battle.get()
            if victor:
                print(f'UID {victor.uid} wins the battle!')
            else:
                print(f'Battle is a tie!')
