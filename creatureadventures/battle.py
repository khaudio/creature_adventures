from creature import *
from player import *
import itertools


class Battle:
    def __init__(self, creature1, creature2):
        self._participants = [creature1, creature2]
        # self._offensiveIndex = 0
        # self._defensiveIndex = 1
        self.actionQueue = collections.deque()

    # @property
    # def attacker(self):
    #     return self._participants[self._offensiveIndex]
    
    # @attacker.setter
    # def attacker(self, participant):
    #     for i, creature in enumerate(self._participants):
    #         if creature == participant:
    #             self._offensiveIndex = i
    #             return
    #     else:
    #         raise ValueError('Creature unavailable')
    
    # @property
    # def defender(self):
    #     return self._participants[self._defensiveIndex]
    
    # @defender.setter
    # def defender(self, participant):
    #     for i, creature in enumerate(self._participants):
    #         if creature == participant:
    #             self._defensiveIndex = i
    #             return
    #     else:
    #         raise ValueError('Creature unavailable')
    
    # def flip_turn(self):
    #     if not self._offensiveIndex:
    #         self._offensiveIndex = 1
    #         self._defensiveIndex = 0
    #     else:
    #         self._offensiveIndex = 0
    #         self._defensiveIndex = 1

    def active(self):
        return (creature.hp > 0 for creature in self._participants)

    def stage_action(self, action):
        self.actionQueue.append(action)

    def process_actions(self):
        # Process actions
        while self.actionQueue and self.active():
            action = self.actionQueue.popleft()
            action.apply()
    
