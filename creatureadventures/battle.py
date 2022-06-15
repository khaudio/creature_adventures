from creature import *
from player import *
import multiprocessing
import itertools


class Battle:
    def __init__(self, attackingCreature, defendingCreature):
        self._participants = [attackingCreature, defendingCreature]
        # self._offensiveIndex = 0
        # self._defensiveIndex = 1
        # self.actionQueue = collections.deque()
        self.actionQueue = multiprocessing.Queue()
        print(f'{attackingCreature} begins a battle with {defendingCreature}')

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
        '''Battle is active while both creatures' HP is nonzero'''
        return all(creature.hp > 0 for creature in self._participants)

    def stage_action(self, action):
        '''Stage a single action in queue for later processing'''
        self.actionQueue.put(action)

    def process_single_action(self, action = None):
        '''Process a single action
        
        May be from queue or provided explicitly as an argument.
        This is useful for special actions, such as those provided by items.
        In normal play, actions should be processed in pairs'''
        action = self.actionQueue.get() if action is None else action
        action.run()
        action.apply()

    def process_action_pair(self):
        '''Process actions in pairs so that combat happens at the same time'''
        if self.actionQueue.empty() or (self.actionQueue.qsize() % 2):
            raise ValueError('Queue size must be multiple of two and not empty')
        for _ in range(2):
            action = self.actionQueue.get()
            action.run()
            action.apply()

    def run(self):
        '''Process all staged actions two at a time until empty'''
        while not self.actionQueue.empty() and self.active():
            self.process_action_pair()
    
    def get(self):
        '''Return victorious creature if there is a winner'''
        if not any(creature.hp > 0 for creature in self._participants):
            # Mutual knockout; tie
            return None
        elif (creature[0].hp > 0) and (creature[1].hp <= 0):
            return creature[0]
        elif (creature[0].hp <= 0) and (creature[1].hp > 0):
            return creature[1]
        else:
            # Both creatures alive but battle ended
            return None

