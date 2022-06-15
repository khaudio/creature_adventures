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
    
    print('\n\n')

    b = Battle(p1.creatures[0], p2.creatures[0])
    s1 = Strike(p1.creatures[0], p2.creatures[0])
    s1.run()
    d1 = Dodge(p2.creatures[0], p1.creatures[0])
    d1.run()
    b.stage_action(s1)
    b.stage_action(d1)
    b.process_actions()
    
    while not any(not c.hp for c in b._participants):
        p1a = Strike(p1.creatures[0], p2.creatures[0])
        p1a.run()
        p2a = Strike(p2.creatures[0], p1.creatures[0])
        p2a.run()

        b.stage_action(p1a)
        b.stage_action(p2a)
        b.process_actions()

    for p in players:
        print(p.creatures[0])


def main():
    print('Starting Adventure...')
    # demo_test()


main()

