from re import A
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
        print(f'UOD {attackingCreature.uid} begins a battle with UID {defendingCreature.uid}')

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

    def match_participant(self, creature):
        for c in self._participants:
            if c.uid == creature.uid:
                return c

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
        self.match_participant(action.invoker).hp = action.invoker.hp
        self.match_participant(action.opponent).hp = action.opponent.hp

    def process_action_pair(self):
        '''Process actions in pairs so that combat happens at the same time'''
        if self.actionQueue.empty() or (self.actionQueue.qsize() % 2):
            raise ValueError('Queue size must be multiple of two and not empty')
        actions = [self.actionQueue.get() for _ in range(2)]
        for a in actions:
            a.run()
        if actions[0].evasive:
            actions[1].evaded = True
        if actions[1].evasive:
            actions[0].evaded = True
        for a in actions:
            a.apply()
            self.match_participant(a.invoker).hp += a.invokerHPDelta
            self.match_participant(a.opponent).hp += a.opponentHPDelta
        print(
                f'\t\tUID {self._participants[0].uid}'
                + f'\tHP = {self._participants[0].hp} / {self._participants[0].maxHP}'
                + f'\n\t\tUID {self._participants[1].uid}'
                + f'\tHP = {self._participants[1].hp} / {self._participants[1].maxHP}\n'
            )

    def run(self):
        '''Process all staged actions two at a time until empty'''
        while self.active() and not self.actionQueue.empty():
            self.process_action_pair()
    
    def get(self):
        '''Return victorious creature if there is a winner'''
        if not any(creature.hp > 0 for creature in self._participants):
            # Mutual knockout; tie
            return None
        elif (self._participants[0].hp > 0) and (self._participants[1].hp <= 0):
            return self._participants[0]
        elif (self._participants[0].hp <= 0) and (self._participants[1].hp > 0):
            return self._participants[1]
        else:
            # Both creatures alive but battle ended
            return None
