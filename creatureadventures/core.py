from battle import *
from deck import *
from dice import *

class CoreBase:
    def __init__(self):
        self.players = []

    def tick_modifiers(self):
        for creature in itertools.chain(p.creatures for p in self.players):
            for modifier in creature.modifiers:
                modifier.numTurns -= 1
                if modifier.numTurns <= 0:
                    creature.remove_modifier(modifier)

