from creature import *
import collections


class PlayerBase:
    def __init__(self, uid, name = None):
        self.uid = uid
        self.name = name
        self.level = 1
        self.creatures = collections.deque(maxlen=3)
        self._activeCreatureIndex = 0
        self.availableActions = []
        self.items = []
        self.assignableAttributePoints = 0
    
    @property
    def activeCreature(self):
        return self.creatures[self._activeCreatureIndex]
    
    @activeCreature.setter
    def activeCreature(self, crt):
        for i, creature in self.creatures:
            if crt == creature:
                self._activeCreatureIndex = i
                return
        else:
            raise ValueError(f'Creature {crt} unavailable to player')

    def has_sigil(self, sigilType):
        return (sigilType in self.items)

    def level_up(self):
        self.level += 1
        self.assignableAttributePoints += self.level
    
    def assign_attack_attribute_points(self, creature):
        if creature in self.creatures:
            creature.attack


class Player(PlayerBase):
    def __init__(self, uid, name = None):
        super().__init__(uid, name)
        self.human = True
        self._catchChance = None
        self._maxCatchChance = None

    @property
    def catchChance(self):
        return self._catchChance
    
    @catchChance.setter
    def catchChance(self, value):
        if not value:
            raise ValueError('Value cannot be zero')
        elif value > self._maxCatchChance:
            value = self._maxCatchChance
        self._catchChance = value


class Warlord(PlayerBase):
    def __init__(self, uid, level):
        super().__init__(uid)
        self.level = level
        self.human = False


class Gladiator(PlayerBase):
    def __init__(self, uid, level):
        super().__init__(uid)
        self.level = level
        self.human = False
