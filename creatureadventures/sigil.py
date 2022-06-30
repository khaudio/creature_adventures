from item import *


class Artifact:

    name = ''
    description = ''

    def __init__(self, uid):
        self.uid = uid


class Sigil(Artifact):

    def __init__(self, uid):
        super().__init__(self, uid)


class SigilOfPower(Sigil):

    name = 'Sigil of Power'
    description = 'Add 3 attack points to a creature you control'

    def __init__(self, uid):
        super().__init__(self, uid)


class SigilOfSpeed(Sigil):

    name = 'Sigil of Speed'
    description = 'You may act first in battle.  After the first attack, all following attacks are simultaneous.'

    def __init__(self, uid):
        super().__init__(self, uid)


class SigilOfWisdom(Sigil):

    name = 'Sigil of Wisdom'
    description = 'Heal one creature for 50% max HP once per turn (or once per battle)'

    def __init__(self, uid):
        super().__init__(self, uid)


class QuietShoes(Artifact):

    name = 'Quiet Shoes'
    description = 'Allows a player to avoid battles with wild creatures'

    def __init__(self, uid):
        super().__init__(self, uid)


