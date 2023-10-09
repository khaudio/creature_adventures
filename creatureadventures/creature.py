from tieredobjectbase import *
import dataclasses

@dataclasses.dataclass
class ModifierBase:
    def __init__(self, numTurns, timed, activeDuringCombat):
        if (numTurns > 0) and (timed is None):
            timed = True
        self.uid = None
        self.numTurns = numTurns
        self.timed = timed
        self.activeDuringCombat = activeDuringCombat


@dataclasses.dataclass
class CreatureModifier(ModifierBase):
    '''
    Modifiers to creature attributes.
    Can optionally expire after
    numTurns if timed is set to True.
    value can be a positive or negative integer.
    '''
    
    def __init__(self, numTurns = 0, timed = None, activeDuringCombat = None):
        super().__init__(numTurns, timed, activeDuringCombat)
        self.attackModifier = 0
        self.defenseModifier = 0
        self.hpModifier = 0


class CreatureBase(TieredObjectBase):
    def __init__(self):
        super().__init__()
        self.baseAttack = 0
        self.baseDefense = 0
        self.baseMaxHP = 1

    def __str__(self):
        return '\n'.join((
                f'Creature UID {self.uid}:',
                f'Tier:\t\t\t{self.tierNames[self.tier]}',
                f'Base Attack:\t{self.baseAttack}',
                f'Base Defense:\t{self.baseDefense}',
                f'Base HP:\t\t{self.baseMaxHP}'
            ))


class Creature(CreatureBase):
    def __init__(self, player = None):
        super().__init__()
        self.owner = player
        self.attackModifier = 0
        self.defenseModifier = 0
        self.hpModifier = 0
        self.baseName, self.nickname = None, None
        
        # Modifiers to attributes
        self.modifiers = []
        
        # Special actions per creature
        self.availableActions = []
        
        self._currentHP = self.maxHP

    def __str__(self):
        return '\n'.join((
                f'Creature UID {self.uid}:',
                f'Name:\t\t{self.name}',
                f'Tier:\t\t{self.tierNames[self.tier]}',
                f'Attack:\t\t{self.attack}',
                f'Defense:\t{self.defense}',
                f'HP:\t\t{self.hp} / {self.maxHP}'
            ))

    @property
    def attack(self):
        return (
                self.baseAttack
                + self.attackModifier
                + sum(m.attackModifier for m in self.modifiers)
            )
    
    @attack.setter
    def attack(self, value):
        if not isinstance(value, int):
            raise TypeError('Must be int')
        self.attackModifier = value - self.baseAttack

    @property
    def _permanentAttack(self):
        return self.baseAttack + self.attackModifier
    
    @_permanentAttack.setter
    def _permanentAttack(self, value):
        self.attack = value

    @property
    def defense(self):
        return (
                self.baseDefense
                + self.defenseModifier
                + sum(m.defenseModifier for m in self.modifiers)
            )
    
    @defense.setter
    def defense(self, value):
        if not isinstance(value, int):
            raise TypeError('Must be int')
        self.defenseModifier = value - self.baseDefense
    
    @property
    def _permanentDefense(self):
        return self.baseDefense + self.defenseModifier
    
    @_permanentDefense.setter
    def _permanentDefense(self, value):
        self.defense = value

    @property
    def maxHP(self):
        return (
                self.baseMaxHP
                + self.hpModifier
                + sum(m.hpModifier for m in self.modifiers)
            )

    @maxHP.setter
    def maxHP(self, value):
        if not isinstance(value, int):
            raise TypeError('Must be int')
        if value <= 0:
            raise ValueError('Must be positive nonzero integer')
        self.hpModifier = value - self.baseMaxHP

    @property
    def hp(self):
        return self._currentHP
    
    @hp.setter
    def hp(self, currentHPValue):
        if not isinstance(currentHPValue, int):
            raise TypeError('Must be int')
        if currentHPValue > self.maxHP:
            currentHPValue = self.maxHP
        elif currentHPValue < 0:
            self._currentHP = 0
        else:
            self._currentHP = currentHPValue

    @property
    def name(self):
        return self.nickname if self.nickname else self.baseName
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Must be str')
        self.nickname = value

    def add_modifier(self, modifier):
        if isinstance(modifier, CreatureModifier):
            self.modifiers.append(modifier)
    
    def remove_modifier(self, modifier):
        for m in self.modifiers:
            if m == modifier:
                self.modifiers.remove(m)
                return

    def heal(self, additionalHP = None):
        if additionalHP is None:
            self.hp = self.maxHP
        else:
            self.hp += additionalHP
