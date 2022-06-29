from creature import *
from player import *
from action import *
from queue import Queue
import itertools


class Battle:
    def __init__(self, attackingCreature, defendingCreature, pvp):
        self._participants = [attackingCreature, defendingCreature]
        self.actionQueue = Queue()

        # True if both players are human
        self.pvp = pvp
        
        print(f'UID {attackingCreature.uid} begins a battle with UID {defendingCreature.uid}')

    def match_participant(self, creature):
        for c in self._participants:
            if c.uid == creature.uid:
                return c

    def active(self):
        '''Battle is active while both creatures' HP is nonzero'''
        return all(creature.hp > 0 for creature in self._participants)

    def stage_action(self, action):
        '''Stage a single action in queue for later processing'''
        action.pvp = self.pvp
        self.actionQueue.put(action)

    def _update_queue_creatures(self, oldCreature, newCreature):
        length = self.actionQueue.qsize()
        for _ in range(length):
            index = None
            action = self.actionQueue.get()
            for i, c in enumerate(action.creatures):
                if c == oldCreature:
                    index = i
            action.creatures[index] = newCreature
            self.actionQueue.put(action)
        else:
            print(f'Updated queue from {oldCreature} to {newCreature}')

    def switch_creatures(self, invoker, target):
        index = None
        for i, creature in self._participants:
            if invoker == creature:
                index = i
        self._participants[index] = target

    def switch_creature_action(self, action):
        if not isinstance(action, Switch):
            raise TypeError('Must be Switch')
        self.switch_creatures(action.invoker, action.target)

    def process_single_action(self, action = None):
        '''Process a single action
        
        May be from queue or provided explicitly as an argument.
        This is useful for single player as well as
        special actions, such as those provided by items.
        In normal pvp play, actions should be processed in pairs'''
        print('Processing single action...')
        action = self.actionQueue.get() if action is None else action
        invoker =  self.match_participant(action.invoker)
        if isinstance(action, Switch):
            self.switch_creature_action(action)
            self._update_queue_creatures(action.invoker, action.target)
            return
        action.run()
        if isinstance(action, ModifierAction):
            invoker.add_modifier(action.get_modifier())
        else:
            results = action.get()
            self.match_participant(action.invoker).hp += results[0]
            self.match_participant(action.target).hp += results[1]

    def process_action_pair(self):
        '''Process actions in pairs so that combat happens at the same time'''
        print('Processing action pair...')
        if self.actionQueue.empty() or (self.actionQueue.qsize() % 2):
            raise ValueError('Queue size must be multiple of two and not empty')
        actions = [self.actionQueue.get() for _ in range(2)]
        if isinstance(actions[0], Switch):
            if actions[1].target == actions[0].invoker:
                actions[1].target = actions[0].target
        if isinstance(actions[1], Switch):
            if not isinstance(actions[0], Switch):
                self.process_single_action(actions[0])
            self.process_single_action(actions[1])
            return
        for a in actions:
            if isinstance(a, ModifierAction):
                a.run()
                invoker = self.match_participant(a.invoker)
                invoker.add_modifier(a.get_modifier())
        for a in actions:
            if not isinstance(a, ModifierAction):
                a.run()
        if actions[0].evasive:
            actions[1].evaded = True
        if actions[1].evasive:
            actions[0].evaded = True
        for a in actions:
            results = a.get()
            self.match_participant(a.invoker).hp += results[0]
            self.match_participant(a.target).hp += results[1]

    def run(self):
        '''Process all staged actions two at a time until empty'''
        while self.active() and not self.actionQueue.empty():
            if self.pvp:
                self.process_action_pair()
            else:
                self.process_single_action()
            print(
                    f'\tUID {self._participants[0].uid}'
                    + f'\tHP = {self._participants[0].hp} / {self._participants[0].maxHP}'
                )
            print(
                    f'\tUID {self._participants[1].uid}'
                    + f'\tHP = {self._participants[1].hp} / {self._participants[1].maxHP}'
                )
    
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
