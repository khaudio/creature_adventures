import random


# Roll dice

def roll_dice(units = 1, sides = 6):
    result = []
    for i in range(self.numUnits):
        currentRoll = random.randint(1, sides + 1)
        print(f'Rolled {currentRoll}')
        result.append(currentRoll)
    return result


@dataclass.dataclass
class Outcome:
    def __init__(self, callback, ratio):
        self.callback = callback
        self.ratio = ratio


class Dice:
    def __init__(self):
        self.outcomes = {}
        self._ratioRemaining = 1.0
    
    def _resolve(self):
        '''Distribute probability equally
        to outcomes with unassigned ratios'''
        unassigned = 0
        for outcome in self.outcomes:
            if outcome.ratio is None:
                unassigned += 1
        calculated = self._ratioRemaining / unassigned
        for outcome in self.outcomes:
            if outcome.ratio is None:
                outcome.ratio = calculated
    
    def add_outcome(self, outcome):
        if (
                outcome.ratio is not None
                and (outcome.ratio <= self._ratioRemaining)
            ):
            self.outcomes.add(outcome)
            self._ratioRemaining -= outcome.ratio
        else:
            raise ValueError('Outcome probability ratio is higher than ratio remaining')
        self._resolve()
    
    def roll(self):
        ratioSum = 0.0
        result = random.random()
        for outcome in self.outcomes:
            if ratioSum <= outcome.ratio < (ratioSum + outcome.ratio):
                return outcome.callback
            ratioSum += outcome.ratio
    
    
