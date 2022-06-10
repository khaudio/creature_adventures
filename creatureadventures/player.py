from creature import *
import collections


class Player:
    def __init__(self, *args, **kwargs):
        self._uid = None
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
