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


class Action:
    '''
    Actions are taken by creatures to cause damage or healing
    during battles
    
    Some actions may be used outside of battle
    '''
    
    def __init__(self, actionName, invoker, opponent = None):
        self.name = actionName
        
        # Creature invoking the action
        self.invoker = invoker
        
        # Creature target of the action
        # Not required as some actions do not require a target
        self.opponent = opponent
        
        # HP gained or lost for each creature.
        # Can be a positive or negative integer
        self.invokerHPDelta = 0
        self.opponentHPDelta = 0
        
        # Did invoker successfully complete an evasive maneuver
        self.evasive = False

        # Did invoker fail to make contact or did opponent evade
        self.evaded = False
        
        # True if both players are human
        self.pvp = None
    
    def offset_opponent_hp(self, opponentHPOffset):
        '''Modifies opponent creature's HP
        
        Positive values add HP (heal),
        negative values remove HP (damage)'''
        self.opponentHPDelta += opponentHPOffset

    def offset_invoker_hp(self, invokerHPOffset):
        '''Modifies action invoking creature's HP
        
        Positive values add HP (heal),
        negative values remove HP (damage)'''
        self.invokerHPDelta += invokerHPOffset

    def damage_opponent(self, opponentHPLost):
        '''Takes positive value as argument
        and applies it as a negative hp offset
        to opponent (damage)'''
        self.opponentHPDelta -= opponentHPLost
    
    def damage_invoker(self, invokerHPLost):
        '''Takes positive value as argument
        and applies it as a negative hp offset
        to invoker (damage)'''
        self.invokerHPDelta -= invokerHPLost

    def run(self):
        '''Process action logic'''

    def get(self):
        '''Return hp deltas to be processed'''
        if self.evaded:
            self.opponentHPDelta = 0
        return (self.invokerHPDelta, self.opponentHPDelta)
    
    def apply(self):
        self.get()
        self.invoker.hp += self.invokerHPDelta
        self.opponent.hp += self.opponentHPDelta


class Strike(Action):
    def __init__(self, atkr, dfndr):
        super().__init__('Strike', atkr, dfndr)
    
    def run(self):
        result = roll_dice(10)
        if result == 1:
            print(f'UID {self.invoker.uid} missed UID {self.opponent.uid}')
            self.evaded = True
            return
        elif result in (2, 3):
            damage = trim_min(self.invoker.attack, 0)
            print(f'UID {self.invoker.uid} hit UID {self.opponent.uid} unmitigated for {damage}')
            self.damage_opponent(damage)
        elif result in range(4, 9):
            damage = trim_min(self.invoker.attack - self.opponent.defense, 0)
            print(f'UID {self.invoker.uid} hit UID {self.opponent.uid} deflected for {damage}')
            self.damage_opponent(damage)
        elif result == 9:
            damage = self.invoker.attack - self.opponent.defense
            counter = self.opponent.attack - self.invoker.defense
            self.damage_opponent(damage)
            self.damage_invoker(counter)
            print(f'UID {self.invoker.uid} struck UID {self.opponent.uid} for {damage}\nUID {self.opponent.uid} counterstruck UID {self.invoker.uid} for {counter}')
        elif result == 10:
            damage = trim_min((self.invoker.attack * 2) - self.opponent.defense, 0)
            print(f'UID {self.invoker.uid} critically hit UID {self.opponent.uid} for {damage}')
            self.damage_opponent(damage)
        print(f'\tUID {self.invoker.uid}\tHP Delta = {self.invokerHPDelta}\n\tUID {self.opponent.uid}\tHP Delta = {self.opponentHPDelta}')


class Meditate(Action):
    def __init__(self, invoker, opponent):
        super().__init__('Meditate', invoker, opponent)
    
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
    def __init__(self, invoker, opponent):
        super().__init__('Brace', invoker, opponent)
    
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
    def __init__(self, invoker, opponent):
        super().__init__('Dodge', invoker, opponent)
    
    def run(self):
        result = roll_dice(10)
        if result in range(1, 7):
            print(f'UID {self.invoker.uid} dodged unsuccessfully')
        else:
            print(f'UID {self.invoker.uid} dodged attack')
            self.evasive = True
    
class InnerPeace(Action):
    def __init__(self, invoker, opponent):
        super().__init__('Inner Peace', invoker, opponent)

    def run(self):
        healAmount = round(self.invoker.hp * 0.5)
        print(f'UID {self.invoker.uid} cast Inner Peace and heals for {healAmount}')
        if self.invoker.hp > 0:
            self.invoker.hp = healAmount


class Switch(Action):
    '''Switch to specified invoker'''
    
    def __init__(self, switchingFrom, switchingTo, *args, **kwargs):
        super().__init__(self, 'Switch', switchingFrom, None, *args, **kwargs)
        self.switch = True
        self.invoker = switchingFrom
        self.switchingTo = switchingTo
