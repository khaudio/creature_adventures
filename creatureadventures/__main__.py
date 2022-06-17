from action import *
from deck import *
from battle import *
from dice import *
from core import *


def demo_test():
    core = CoreBase()
    # core.create_warlords()
    # core.create_gladiator()
    
    deck = create_creature_deck(25)

    p1 = Player()
    p2 = Player()

    players = [p1, p2]

    for p in players:
        for _ in range(3):
            p.creatures.append(deck.draw())
        print(p.creatures[0])
    
    print('\n')
    input('press Enter to batlle...')

    c1 = p1.creatures[0]
    c2 = p2.creatures[0]

    b = Battle(c1, c2, pvp = True)
    b.stage_action(Strike(c1, c2))
    b.stage_action(Dodge(c2, c1))
    
    b.stage_action(Meditate(c1, c2))
    b.stage_action(Brace(c2, c1))

    while b.active():
        b.stage_action(Strike(c1, c2))
        b.stage_action(Strike(c2, c1))
        b.run()
    
    victor = b.get()
    if victor is None:
        print('Battle is a tie!')
    else:
        print(f'Battle victor: UID {victor.uid}\n')

    print(c1, '\n', c2, '\n')


def main():
    print('Starting Adventure...')
    demo_test()
    
    


main()

