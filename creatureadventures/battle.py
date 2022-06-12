from creature import *
from player import *


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


class Battle:
    def __init__(self, *args, **kwargs):
        self._players = []
        self._offensiveIndex = 0
        self._defensiveIndex = 1

    @property
    def attacker(self):
        return self._players[self._offensiveIndex]
    
    @attacker.setter
    def attacker(self, player):
        for i, plyr in enumerate(self._players):
            if plyr == player:
                self._offensiveIndex = i
                return
        else:
            raise ValueError('Player unavailable')
    
    @property
    def defender(self):
        return self._players[self._defensiveIndex]
    
    @defender.setter
    def defender(self, player):
        for i, plyr in enumerate(self._players):
            if plyr == player:
                self._defensiveIndex = i
                return
        else:
            raise ValueError('Player unavailable')
    
    def flip_turn(self):
        if not self._offensiveIndex:
            self._offensiveIndex = 1
            self._defensiveIndex = 0
        else:
            self._offensiveIndex = 0
            self._defensiveIndex = 1

    def strike(self):
        result = roll(1, 10)
        if result == 1:
            print('Miss')
            return 0
        elif result in (2, 3):
            print('Unmitigated hit')
            return self.attacker.attack
        elif result in range(4, 9):
            print('Deflected hit')
            damage = self.attacker.attack - self.defender.defense
            return trim_min(damage, 0)
        elif result == 9:
            print('Counterstrike')
            damage = self.attacker.defense - self.defender.attack
            return trim_min(damage, 0)
        elif result == 10:
            print('Critical hit')
            damage = (self.attacker.attack * 2) - self.defender.defense
            return trim_max(damage, 0)

    def meditate(self):
        result = roll(1, 10)
        if result == 1:
            print('No change to attack')
            return 0
        elif result in range(2, 7):
            pass


    def stage_action(self, player, action):
        pass

    def process_actions(self):
        pass


