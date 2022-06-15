from dice import *


class Action:
    '''
    Actions are taken by creatures to cause damage or healing
    during battles
    
    Some actions may be used outside of battle
    '''
    
    def __init__(self, actionName, atkr, dfndr):
        self.name = actionName
        
        # Creature invoking the action
        self.attacker = atkr
        
        # Creature target of the action
        self.defender = dfndr
        
        # HP gained or lost for each creature.
        # Can be a positive or negative integer
        self.attackerHPDelta = 0
        self.defenderHPDelta = 0
    
    def offset_defender_hp(self, defenderHPOffset):
        '''Modifies defending creature's HP
        
        Positive values add HP (heal),
        negative values remove HP (damage)'''
        self.defenderHPDelta += defenderHPOffset

    def offset_attacker_hp(self, attackerHPOffset):
        '''Modifies defending creature's HP
        
        Positive values add HP (heal),
        negative values remove HP (damage)'''
        self.attackerHPDelta += attackerHPOffset

    def damage_defender(self, defenderHPLost):
        '''Takes positive value as argument
        and applies it as a negative hp offset
        to defender (damage)'''
        self.defenderHPDelta -= defenderHPLost
    
    def damage_attacker(self, attackerHPLost):
        '''Takes positive value as argument
        and applies it as a negative hp offset
        to attacker (damage)'''
        self.attackerHPDelta -= attackerHPLost

    def run(self):
        '''Process action logic'''

    def get(self):
        '''Return hp deltas to be processed'''
        return (self.attackerHPDelta, self.defenderHPDelta)


class Strike(Action):
    def __init__(self, atkr, dfndr):
        super().__init__('Strike', atkr, dfndr)
    
    def run(self):
        result = roll_dice(1, 10)
        if result == 1:
            print('Miss')
            return 0
        elif result in (2, 3):
            print('Unmitigated hit')
            damage = trim_min(self.attacker.attack, 0)
            self.damage_defender(damage)
        elif result in range(4, 9):
            print('Deflected hit')
            damage = trim_min(self.attacker.attack - self.defender.defense, 0)
            self.damage_defender(damage)
        elif result == 9:
            print('Counterstrike')
            damage = self.attacker.attack - self.defender.attack
            if damage > 0:
                self.damage_defender(damage)
            elif damage < 0:
                self.offset_attacker_hp(damage)
        elif result == 10:
            print('Critical hit')
            damage = trim_min((self.attacker.attack * 2) - self.defender.defense, 0)
            self.damage_defender(damage)


class Meditate(Action):
    def __init__(self, atkr, dfndr):
        super().__init__('Meditate', atkr, dfndr)
    
    def run(self):
        result = roll_dice(1, 10)
        if result == 1:
            print('No change to attack')
            return 0
        elif result in range(2, 7):
            self.attacker.add_timed_modifier()


