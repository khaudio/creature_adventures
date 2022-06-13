from tieredobjectbase import *
import dataclass


class CreatureBase(TieredObjectBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.baseAttack = 0
        self.baseDefense = 0
        self.baseHP = 1

    def __str__(self):
        return '\n'.join((
                f'Creature UID {self.uid}:',
                f'Tier:\t\t\t\t\t{self.tierNames[self.tier]}',
                f'Base Attack:\t{self.baseAttack}',
                f'Base Defense:\t{self.baseDefense}',
                f'Base HP:\t\t\t{self.baseHP}'
            ))


@dataclass.dataclass
class TimedModifier:
    '''
    Modifiers to creatures that expire after numTurns.
    value can be a positive or negative integer.
    '''
    
    def __init__(self):
        self.numTurns = 0
        self.attackModifier = 0
        self.defenseModifier = 0
        self.hpModifier = 0


class Creature(CreatureBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attackModifier = 0
        self.defenseModifier = 0
        self.hpModifier = 0
        
        # Modifiers that expire after a specified number of turns
        self.timedModifiers = []
        
        # Special actions per creature
        self.availableActions = []
    
    @property
    def attack(self):
        return (
                self.baseAttack
                + self.attackModifier
                + sum(m.attackModifier for m in self.timedModifiers)
            )
    
    @attack.setter
    def attack(self, attrPoints):
        if not isinstance(attrPoints, int):
            raise TypeError('Must be int')
        self.attackModifier = attrPoints

    @property
    def defense(self):
        return (
                self.baseDefense
                + self.defenseModifier
                + (m.defenseModifier for m in self.timedModifiers)
            )
    
    @defense.setter
    def defense(self, attrPoints):
        if not isinstance(attrPoints, int):
            raise TypeError('Must be int')
        self.defenseModifier = attrPoints
    
    @property
    def hp(self):
        return (
                self.baseHP
                + self.hpModifier
                + (m.hpModifier for m in self.timedModifiers)
    
    @hp.setter
    def hp(self, attrPoints):
        if not isinstance(attrPoints, int):
            raise TypeError('Must be int')
        self.hpModifier = 2 * attrPoints


