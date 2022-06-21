from action import *
from deck import *
from battle import *
from dice import *
from core import *


def demo_test():
    core = CoreBase()

    p1 = Player()
    p2 = Player()

    core.players = [p1, p2]

    for p in core.players:
        for _ in range(3):
            p.creatures.append(core.draw())
        print(p.creatures[0])
    
    print('\n')
    input('press Enter to battle...')

    c1 = p1.creatures[0]
    c2 = p2.creatures[0]

    core.run_battle(c1, c2, pvp = True)

    print(c1, '\n', c2, '\n')


def main():
    print('Starting Adventure...')
    demo_test()


main()

