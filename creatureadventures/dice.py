import random
import dataclasses

# Roll dice

def roll_dice(sides = 6):
    return random.randint(1, sides)


class Outcome:
    def __init__(self, callback, ratio = None):
        self.callback = callback
        self.ratio = ratio
        self._upperThreshold = None

    @property
    def ratio(self):
        return self._ratio
    
    @ratio.setter
    def ratio(self, value = None):
        self._ratio = value
        self._auto = True if value is None else False

class Dice:
    def __init__(self):
        # All possible outcomes for this roll
        self.outcomes = []

        # Max for all combined outcome ratios is 1.0
        self._ratioTotal = 0.0
    
    def _resolve(self):
        '''Distribute probability equally
        to outcomes with unassigned ratios'''
        unassigned = 0
        for outcome in self.outcomes:
            if outcome.ratio is None:
                unassigned += 1
        calculated = self._ratioTotal / unassigned
        for outcome in self.outcomes:
            if outcome._auto:
                outcome.ratio = calculated
            outcome._upperThreshold =  self._ratioTotal + outcome.ratio
            self._ratioTotal -= outcome.ratio
        if self._ratioTotal > 1.0:
            raise ValueError(
                    'Outcome probability ratio is higher'
                    + ' than remaining probability available'
                )
        self.outcomes.sort(key=outcome._upperThreshold)

    def add_outcomes(self, *outcomes):
        for outcome in outcomes:
            self.outcomes.append(outcome)
        self._resolve()
    
    def roll(self):
        lowerThreshold = 0.0
        result = random.random()
        print(f'Rolled {result}')
        for outcome in self.outcomes:
            if lowerThreshold <= result < outcome._upperThreshold:
                return outcome.callback
            lowerThreshold = outcome._upperThreshold

