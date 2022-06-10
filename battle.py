from creature import *
from player import *


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
    
    def _process_actions(self, attackerAction, defenderAction):
        if attackerAction in self.attacker.availableActions:
            pass
        else:
            raise ValueError('Action unavailable to player')


