from battle import *
from deck import *
from dice import *


class CoreBase:
    # Default max stat points available for all creature creation
    maxPossibleStatPoints = 30
    maxPossibleCatchChance = maxPossibleStatPoints / 5
    globalActions = [
            Strike,
            Meditate,
            Brace,
            Dodge,
            Switch,
            Forfeit,
            Escape
        ]
    _allActions = [
            *globalActions,
            Pass,
            Catch
        ]
    
    def __init__(self, shuffle=True):
        self._uidIndex = 1
        self.players = []
        self.warlords = []
        self.gladiator = None
        
        self.creatureDeck = create_creature_deck(
                50, # Size of creature deck
                self.maxPossibleStatPoints
            )
        self.itemDeck = create_item_deck(
                50, # Size of item deck
                self.maxPossibleStatPoints
            )
        
        self.creatureDeck.reset_uids(index = self._uidIndex)
        self._uidIndex += len(self.creatureDeck)
        self.itemDeck.reset_uids(index = self._uidIndex)
        self._uidIndex += len(self.itemDeck)

        if shuffle:
            self.creatureDeck.shuffle()
            self.itemDeck.shuffle()

    def create_player(self, name = None):
        newPlayer = Player(uid=self._uidIndex, name=name)
        self._uidIndex += 1

        # Default to 30% chance of catching wild creatures
        newPlayer._maxCatchChance = self.maxPossibleCatchChance
        newPlayer.catchChance = round(self.maxPossibleCatchChance / 3)
        
        self.players.append(newPlayer)
        return newPlayer

    def draw_creature(self):
        return self.creatureDeck.draw()
    
    def draw_item(self):
        return self.itemDeck.draw()

    def tick_modifiers(self):
        for p in self.players:
            for creature in p.creatures:
                for modifier in creature.modifiers:
                    if not modifier.timed:
                        continue
                    modifier.numTurns -= 1
                    print(f'Modifier on UID {creature.uid} has {modifier.numTurns} remaining')
                    if modifier.numTurns <= 0:
                        creature.remove_modifier(modifier)
    
    def remove_combat_modifiers(self):
        '''Run this after combat is completed to remove untimed temporary modifiers'''
        print('Removing combat modifiers')
        for p in self.players:
            for creature in p.creatures:
                for modifier in creature.modifiers:
                    if modifier.activeDuringCombat:
                        creature.remove_modifier(modifier)
    
    def create_warlords(self):
        for _ in range(3):
            self.warlords.append(Warlord(self._uidIndex, 2))
            self._uidIndex += 1
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
        self.gladiator = Gladiator(self._uidIndex, 3)
        self._uidIndex += 1
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

    def match_player(self, player):
        for p in self.players:
            if p.uid == player.uid:
                return p

    def match_creature(self, creature):
        for player in self.players:
            for c in player.creatures:
                if c.uid == creature.uid:
                    return c

    def get_creature(self, creatureUID):
        for player in self.players:
            for c in player.creatures:
                if c.uid == creatureUID:
                    return c

    @staticmethod
    def match_item(player, item):
        for i in player.items:
            if i.uid == item.uid:
                return i

    def use_item(self, invokingPlayer, item, itemTarget = None):
        matchedPlayer = self.match_player(invokingPlayer)
        matchedItem = self.match_item(matchedPlayer, item)
        matchedCreature = self.match_creature(itemTarget)

        if isinstance(item, Net):
            matchedPlayer.catchChance += matchedItem.get()
            return
        elif not isinstance(itemTarget, Creature):
            raise TypeError('Must be used on Creature')
        if not matchedItem:
            raise ValueError('Item not found in player inventory')


        if isinstance(item, Potion):
            if matchedCreature.hp <= 0:
                raise ValueError('Target HP must be > 0')
            matchedCreature.hp += matchedItem.get()
        elif isinstance(item, Poison):
            matchedCreature.hp += matchedItem.get()
        elif isinstance(item, Revive):
            if matchedCreature.hp > 0:
                raise ValueError('Target HP must be zero')
            matchedCreature.hp = item.get()
        elif isinstance(item, Elixir):
            mod = CreatureModifier(activeDuringCombat=True)
            mod.attackModifier += matchedItem.get()
            matchedCreature.add_modifier(mod)
        
        # Consume item unless persistent
        if not matchedItem.persistent:
            matchedPlayer.items.remove(matchedItem)

