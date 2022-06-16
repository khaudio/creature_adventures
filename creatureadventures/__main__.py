from action import *
from deck import *
from battle import *
from dice import *
from core import *


def demo_test():
    deck = create_creature_deck(25)

    p1 = Player()
    p2 = Player()

    players = [p1, p2]

    for p in players:
        for _ in range(3):
            p.creatures.append(deck.draw())
        print(p.creatures[0])
    
    print('\n')

    p1C = p1.creatures[0]
    p2C = p2.creatures[0]

    b = Battle(p1C, p2C)
    b.stage_action(Strike(p1C, p2C))
    b.stage_action(Dodge(p2C, p1C))
    
    while b.active():
        b.stage_action(Strike(p1C, p2C))
        b.stage_action(Strike(p2C, p1C))
        b.run()
    
    victor = b.get()
    print(f'Battle victor: UID {victor.uid}\n')

    print(p1C, '\n', p2C, '\n')


def main():
    print('Starting Adventure...')
    demo_test()


main()

