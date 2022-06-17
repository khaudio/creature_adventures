from creature import TimedModifier
from dice import *


def trim_min(value, minimum):
    if value < minimum:
        return minimum
    else:
        return value


def trim_max(value, maximum):
    if value > maximum:
        return maximum
    else:
        return value


class ActionBase:
    '''Base class for Actions'''

    def __init__(self, actionName, invoker, target = None):
        self.name = actionName
        
        # Creature invoking the action
        self.invoker = invoker

        # Creature target of the action (invoker may target itself)
        self.target = target

        # True if both players are human
        self.pvp = None

    def run(self):
        '''Process action logic'''

    def get(self):
        '''Return HP deltas to be processed'''
    
    def apply(self):
        '''Reconcile HP deltas'''


class Action(ActionBase):
    '''
    Actions are taken by creatures to cause damage or healing
    during battles
    
    Some actions may be used outside of battle
    '''
    
    def __init__(self, actionName, invoker, target = None):
        super().__init__(actionName, invoker, target)

        # HP gained or lost for each creature.
        # Can be a positive or negative integer
        self.invokerHPDelta = 0
        self.targetHPDelta = 0
        
        # Did invoker successfully complete an evasive maneuver
        self.evasive = False

        # Did invoker fail to make contact or did target evade
        self.evaded = False
    
    def offset_target_hp(self, targetHPOffset):
        '''Modifies target creature's HP
        
        Positive values add HP (heal),
        negative values remove HP (damage)'''
        self.targetHPDelta += targetHPOffset

    def offset_invoker_hp(self, invokerHPOffset):
        '''Modifies action invoking creature's HP
        
        Positive values add HP (heal),
        negative values remove HP (damage)'''
        self.invokerHPDelta += invokerHPOffset

    def damage_target(self, targetHPLost):
        '''Takes positive value as argument
        and applies it as a negative hp offset
        to target (damage)'''
        self.targetHPDelta -= targetHPLost
    
    def damage_invoker(self, invokerHPLost):
        '''Takes positive value as argument
        and applies it as a negative hp offset
        to invoker (damage)'''
        self.invokerHPDelta -= invokerHPLost
    
    def get(self):
        '''Return hp deltas to be processed'''
        if self.evaded:
            self.targetHPDelta = 0
        return (self.invokerHPDelta, self.targetHPDelta)
    
    def apply(self):
        self.get()
        self.invoker.hp += self.invokerHPDelta
        self.target.hp += self.targetHPDelta


class Strike(Action):
    def __init__(self, invoker, target):
        super().__init__('Strike', invoker, target)
    
    def run(self):
        result = roll_dice(10)
        if result == 1:
            print(f'UID {self.invoker.uid} missed UID {self.target.uid}')
            self.evaded = True
            return
        elif result in (2, 3):
            damage = trim_min(self.invoker.attack, 0)
            print(f'UID {self.invoker.uid} hit UID {self.target.uid} unmitigated for {damage}')
            self.damage_target(damage)
        elif result in range(4, 9):
            damage = trim_min(self.invoker.attack - self.target.defense, 0)
            print(f'UID {self.invoker.uid} hit UID {self.target.uid} deflected for {damage}')
            self.damage_target(damage)
        elif result == 9:
            damage = self.invoker.attack - self.target.defense
            counter = self.target.attack - self.invoker.defense
            self.damage_target(damage)
            self.damage_invoker(counter)
            print(f'UID {self.invoker.uid} struck UID {self.target.uid} for {damage}...\nUID {self.target.uid} counterstruck UID {self.invoker.uid} for {counter}')
        elif result == 10:
            damage = trim_min((self.invoker.attack * 2) - self.target.defense, 0)
            print(f'UID {self.invoker.uid} critically hit UID {self.target.uid} for {damage}')
            self.damage_target(damage)
        print(f'\tUID {self.invoker.uid}\tHP Delta = {self.invokerHPDelta}\n\tUID {self.target.uid}\tHP Delta = {self.targetHPDelta}')


class Meditate(Action):
    def __init__(self, invoker, target):
        super().__init__('Meditate', invoker, target)
    
    def run(self):
        result = roll_dice(10)
        if result == 1:
            print(f'No change to UID {self.invoker.uid} attack')
            return
        attackBoost = TimedModifier()
        attackBoost.numTurns = 1
        if result in range(2, 7):
            print(f'UID {self.invoker.uid} attack raised by 30%')
            attackBoost.attackModifier = round(self.invoker.attack * 0.3)
        elif result in range(7, 10):
            print(f'UID {self.invoker.uid} attack raised by 50%')
            attackBoost.attackModifier = round(self.invoker.attack * 0.5)
        elif result == 10:
            print(f'UID {self.invoker.uid} attack raised by 100%')
            attackBoost.attackModifier = self.invoker.attack * 2
        self.invoker.add_modifier(attackBoost)


class Brace(Action):
    def __init__(self, invoker, target):
        super().__init__('Brace', invoker, target)
    
    def run(self):
        result = roll_dice(10)
        if result == 1:
            print(f'No change to UID {self.invoker.uid} defense')
            return
        defenseBoost = TimedModifier()
        defenseBoost.numTurns = 1
        if result in range(2, 7):
            print(f'UID {self.invoker.uid} defense raised by 30%')
            defenseBoost.defenseModifier = round(self.invoker.defense * 0.3)
        elif result in range(7, 10):
            print(f'UID {self.invoker.uid} defense raised by 50%')
            defenseBoost.defenseModifier = round(self.invoker.defense * 0.5)
        elif result == 10:
            print(f'UID {self.invoker.uid} defense raised by 100%')
            defenseBoost.defenseModifier = self.invoker.defense
        self.invoker.add_modifier(defenseBoost)


class Dodge(Action):
    def __init__(self, invoker, target):
        super().__init__('Dodge', invoker, target)
    
    def run(self):
        result = roll_dice(10)
        if result in range(1, 7):
            print(f'UID {self.invoker.uid} attempted to dodge unsuccessfully')
        else:
            print(f'UID {self.invoker.uid} dodged attack')
            self.evasive = True
    
class InnerPeace(Action):
    def __init__(self, invoker, target):
        super().__init__('Inner Peace', invoker, target)

    def run(self):
        healAmount = round(self.invoker.hp * 0.5)
        print(f'UID {self.invoker.uid} cast Inner Peace and heals for {healAmount}')
        if self.invoker.hp > 0:
            self.invoker.hp = healAmount


class Switch(ActionBase):
    '''Switch from invoker to target as active creature'''
    
    def __init__(self, invoker, target):
        super().__init__(self, 'Switch', invoker, target)

