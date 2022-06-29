import json
from deck import *
from action import *
from core import *


def serialize_creature(creature):
    return {creature.uid : {
            'tier' : creature.tier,
            'attack' : creature.baseAttack,
            'defense' : creature.baseDefense,
            'hp' : creature.maxHP,
            'actions' : creature.availableActions
        }}


def serialize_creature_deck(deck):
    serialized = {'creatures': dict()}
    for creature in deck:
        serialized['creatures'].update(serialize_creature(creature))
    return serialized


def save_creature_deck_as_json(deck, filename):
    with open(filename, 'w') as f:
        serialized = serialize_creature_deck(deck)
        json.dump(serialized, f, indent=4)


def load_creature_deck_from_json(filename):
    with open(filename, 'r') as f:
        serialized = json.load(f)
        deck = Deck()
        for cuid, stats in serialized['creatures'].items():
            creature = Creature()
            creature.uid = int(cuid)
            creature.tier = int(stats['tier'])
            creature.baseAttack = int(stats['attack'])
            creature.baseDefense = int(stats['defense'])
            creature.baseMaxHP = int(stats['hp'])
            for found, indexed in zip(stats['actions'], CoreBase._allActions):
                if found == indexed.name:
                    creature.availableActions.append(indexed)
            creature.heal()
            deck.append(creature)
    return deck

