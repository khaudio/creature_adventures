


class TieredObjectBase:
    tierNames = ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary')

    # Relative ratios of how many objects of each tier should be created.
    # No Epic or Legendary objects by default
    tieredVolumeRatios = {0: 0.58, 1: 0.28, 2: 0.14, 3: 0.00, 4: 0.00}

    # Relative ratios of stat points available to items in each tier
    tierQualityThresholds = {
            0: [0.50, 0.56],
            1: [0.56, 0.63],
            2: [0.63, 0.70],
            3: [0.70, 0.80],
            4: [0.80, 1.00]
        }

    def __init__(self, *args, **kwargs):
        self.uid = None
        self.tier = None
