import random


# Roll dice

def roll(units = 1, sides = 6):
    for i in range(self.numUnits):
        currentRoll = random.randint(1, sides)
        print(f'Rolled {currentRoll}')
        yield currentRoll


