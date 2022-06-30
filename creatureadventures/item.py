from tieredobjectbase import *


class Item(TieredObjectBase):

    name = ''
    description = ''

    # Override from parent class
    tierQualityThresholds = {
            0: [0.22, 0.22],
            1: [0.34, 0.34],
            2: [0.67, 0.67],
            3: [0.80, 0.80],
            4: [1.00, 1.00]
        }

    def __init__(self, tier, maxPossibleValue, persistent = False, uid = None):
        super().__init__()

        self.tier = tier
        self.uid = uid

        # Whether item is persistent after use
        self.persistent = persistent

        # Positive or negative integer
        self.value = round(
                self.tierQualityThresholds[tier][0]
                * maxPossibleValue
            )
    
    def __str__(self):
        return '\n'.join((
                f'Item UID {self.uid}:',
                f'Tier:\t\t{self.tierNames[self.tier]}',
                f'Type:\t\t{self.name}',
                f'Value:\t\t{self.value}'
            ))

    def get(self):
        return self.value

    def value_description(self):
        return []


class Potion(Item):

    name = 'Potion'
    description = 'Heals a creature for a specified amount'

    def __init__(self, tier, maxPossibleValue, persistent = False, uid = None):
        super().__init__(tier, maxPossibleValue, persistent, uid)
        
    def value_description_list(self):
        return [f'Heal a creature for {self.value} HP']


class Poison(Item):

    name = 'Poison'
    description = 'Poisons an enemy creature for unmitigated damage'

    def __init__(self, tier, maxPossibleValue, persistent = False, uid = None):
        super().__init__(tier, maxPossibleValue, persistent, uid)

    def value_description_list(self):
        return [
                f'Damage a creature for {self.value} HP',
                'Ignores defense'
            ]


class Elixir(Item):

    name = 'Elixir'
    description = 'Raises attack or defense power of a creature'
    
    def __init__(self, tier, maxPossibleValue, persistent = False, uid = None):
        super().__init__(tier, maxPossibleValue, persistent, uid)

    def value_description_list(self):
        return [
                f'Raise attack power of a creature by {self.value}',
                f'Lasts until end of battle'
            ]


class Revive(Item):

    name = 'Revive'
    description = 'Revives a creature with depleted HP'

    def __init__(self, tier, maxPossibleValue, persistent = False, uid = None):
        super().__init__(tier, maxPossibleValue, persistent, uid)

    def value_description_list(self):
        return [
                f'Revive a creature with 0 HP'
            ]


class Net(Item):
    
    name = 'Net'
    description = 'Raises chances of successfully catching wild creatures'

    def __init__(self, tier, maxPossibleValue, persistent = False, uid = None):
        super().__init__(tier, maxPossibleValue, persistent, uid)

