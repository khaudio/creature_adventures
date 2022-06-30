

class TieredObjectBase:
    tierNames = ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary')

    # Relative ratios of how many objects of each tier should be created.
    # No Legendary objects by default
    tieredVolumeRatios = {0: 0.56, 1: 0.26, 2: 0.12, 3: 0.06, 4: 0.00}

    # Relative ratios of stat points available to items in each tier
    tierQualityThresholds = {
            0: [0.50, 0.56],
            1: [0.56, 0.63],
            2: [0.63, 0.70],
            3: [0.70, 0.80],
            4: [0.80, 1.00]
        }
    
    if sum(tieredVolumeRatios.values()) != 1.0:
        raise ValueError('Sum must equal 1.0')

    def __init__(self):
        self.uid = None
        self.tier = None

    @property
    def tierName(self):
        return self.tierNames[self.tier]
    
    @tierName.setter
    def tierName(self, value):
        for i, name in enumerate(self.tierNames):
            if value == name:
                self.tier = i
                return
        raise IndexError(f'{name} not found in available tier names')

