from dice import *
from creature import *
from tieredobjectbase import *


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

    name = ''
    description = ''

    def __init__(self, invoker, target = None):
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


class ModifierAction:
    def __init__(self):
        self.modifier = None

    def get_modifier(self):
        return self.modifier


class Action(ActionBase):
    '''
    Actions are taken by creatures to cause damage or healing
    during battles
    
    Some actions may be used outside of battle
    '''

    name = ''
    
    def __init__(self, invoker, target = None):
        super().__init__(invoker, target)

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


class TieredAction(Action, TieredObjectBase):
    def __init__(self, invoker, target):
        super().__init__(invoker, target)
        TieredObjectBase.__init__(self)


class Strike(Action):
    name = 'Strike'
    description = 'Attack an enemy for damage'

    def __init__(self, invoker, target):
        super().__init__(invoker, target)
    
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


class Meditate(Action, ModifierAction):
    name = 'Meditate'
    description = 'Roll to increase attack'

    def __init__(self, invoker, target):
        super().__init__(invoker, target)
        ModifierAction.__init__(self)
    
    def run(self):
        result = roll_dice(10)
        if result == 1:
            print(f'No change to UID {self.invoker.uid} attack')
            return
        self.modifier = TimedModifier()
        # Set numTurns to 2 so that attack is raised on next turn.
        # First turn is used by performing this action itself.
        self.modifier.numTurns = 2
        if result in range(2, 7):
            self.modifier.attackModifier = round(self.invoker._permanentAttack * 0.3)
            print(f'UID {self.invoker.uid} attack raised by 30% to {self.invoker.attack + self.modifier.attackModifier}')
        elif result in range(7, 10):
            self.modifier.attackModifier = round(self.invoker._permanentAttack * 0.5)
            print(f'UID {self.invoker.uid} attack raised by 50% to {self.invoker.attack + self.modifier.attackModifier}')
        elif result == 10:
            self.modifier.attackModifier = self.invoker._permanentAttack
            print(f'UID {self.invoker.uid} attack raised by 100% to {self.invoker.attack + self.modifier.attackModifier}')


class Brace(Action, ModifierAction):
    name = 'Brace'
    description = 'Roll to increase defense'

    def __init__(self, invoker, target):
        super().__init__(invoker, target)
        ModifierAction.__init__(self)
    
    def run(self):
        result = roll_dice(10)
        if result == 1:
            print(f'No change to UID {self.invoker.uid} defense')
            return
        self.modifier = TimedModifier()
        # Set numTurns to 2 so that defense is raised on next turn.
        # First turn is used by performing this action itself.
        self.modifier.numTurns = 2
        if result in range(2, 7):
            self.modifier.defenseModifier = round(self.invoker._permanentDefense * 0.5)
            print(f'UID {self.invoker.uid} defense raised by 50% to {self.invoker.defense + self.modifier.defenseModifier}')
        elif result in range(7, 10):
            self.modifier.defenseModifier = self.invoker._permanentDefense
            print(f'UID {self.invoker.uid} defense raised by 100% to {self.invoker.defense + self.modifier.defenseModifier}')
        elif result == 10:
            self.modifier.defenseModifier = self.invoker._permanentDefense * 2
            print(f'UID {self.invoker.uid} defense raised by 200% to {self.invoker.defense + self.modifier.defenseModifier}')


class Dodge(Action):
    name = 'Dodge'
    description = 'Roll to evade incoming attack'

    def __init__(self, invoker, target):
        super().__init__(invoker, target)
    
    def run(self):
        result = roll_dice(10)
        if result in range(1, 7):
            print(f'UID {self.invoker.uid} attempted to dodge unsuccessfully')
        else:
            print(f'UID {self.invoker.uid} dodged attack')
            self.evasive = True


class InnerPeace(Action):
    name = 'Inner Peace'
    description = 'Heal for half max HP'

    def __init__(self, invoker, target):
        super().__init__(invoker, target)

    def run(self):
        self.invokerHPDelta = round(self.invoker.hp * 0.5)
        print(f'UID {self.invoker.uid} cast Inner Peace and heals for {self.invokerHPDelta}')


class Switch(ActionBase):
    '''Switch from invoker to target as active creature'''

    name = 'Switch'
    description = 'Switch to another creature'
    
    def __init__(self, invoker, target):
        super().__init__(invoker, target)


class Forfeit(ActionBase):

    name = 'Forfeit'
    description = 'Concede defeat and end the battle'

    def __init__(self, invoker, target):
        super().__init__(invoker, target)


class Escape(ActionBase):

    name = 'Escape'
    description = 'Run from battle'

    def __init__(self, invoker, target):
        super().__init__(invoker, target)

