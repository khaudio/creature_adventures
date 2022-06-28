from action import *
from deck import *
from battle import *
from dice import *
from core import *
from cli import *
from pdfcards import *
from saver import *
from item import *
import pathlib


def run_battle(core, attackingCreature, defendingCreature, pvp):
    print(f'Creating {"pvp" if pvp else "pve"} battle...')
    battle = Battle(attackingCreature, defendingCreature, pvp)
    while battle.active():
        print('Cycling battle turn...')
        core.tick_modifiers()
        for creature in battle._participants:
            print(
                    f'UID {creature.uid} has'
                    + f'{len(creature.modifiers)} active modifiers'
                )
        c1, c2 = battle._participants
        selection = prompt_for_action(core, c1)
        action = selection(c1, c2)
        battle.stage_action(action)
        if battle.pvp:
            counterSelection = prompt_for_action(core, c2)
            counterAction = counterSelection(c2, c1)
            battle.stage_action(counterAction)
        battle.run()
        yield
    else:
        print('Battle is over')
        victor = battle.get()
        if victor:
            print(f'UID {victor.uid} wins the battle!')
        else:
            print(f'Battle is a tie!')


def demo_test(core):
    p1, p2 = Player(), Player()
    core.players = [p1, p2]

    for p in core.players:
        card = core.draw()
        while not card.tier == 3:
            card = core.draw()
        card.owner = p
        p.creatures.append(card)
        print(p.creatures[0])

    print('\n')
    input('press Enter to battle...')

    c1, c2 = p1.creatures[0], p2.creatures[0]

    b = run_battle(core, c1, c2, pvp = True)

    while True:
        try:
            next(b)
        except StopIteration:
            break

    print(c1, '\n', c2, '\n')


def load_saved_creatures(path='.'):
    cwd = pathlib.Path(path)
    build = None
    for item in cwd.iterdir():
        if item.name == 'creature_deck.json':
            return load_creature_deck_from_json(item.as_posix())
        elif item.name == 'build' and item.is_dir():
            build = item
    else:
        try:
            return load_saved_creatures(build.as_posix())
        except:
            return


def get_deck(core, override=False):
    # Attempt to load a saved creature deck
    deck = None
    if not override:
        try:
            deck = load_saved_creatures('build')
        except:
            override=True
    if override:
        # Create deck if a saved one could not be loaded
        deck = core.creatureDeck
        save_creature_deck_as_json(deck, './build/creature_deck.json')
        write_creature_pdf_from_deck(
                deck,
                filename='./build/creature_cards.pdf',
                images='./images'
            )
    
    return deck


def main():
    print('Starting Adventure...')
    
    core = CoreBase(shuffle=False)
    core.creatureDeck = get_deck(core, override=False)

    demo_test(core)


main()
