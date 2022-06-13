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

    def stage_action(self, player, action):
        pass

    def process_actions(self):
        pass


