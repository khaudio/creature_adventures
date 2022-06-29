import PyInquirer
from core import *


cliStyle = PyInquirer.style_from_dict({
    PyInquirer.Token.Separator: '#cc5454',
    PyInquirer.Token.QuestionMark: '#673ab7 bold',
    PyInquirer.Token.Selected: '#cc5454',
    PyInquirer.Token.Pointer: '#673ab7 bold',
    PyInquirer.Token.Instruction: '',
    PyInquirer.Token.Answer: '#f44336 bold',
    PyInquirer.Token.Question: '',
})


def prompt_for_target(core, player):
    creatureList = [{
            'type': 'list',
            'message': 'Choose an target',
            'name': 'target',
            'choices': []
        }]

    for creature in player.creatures:
        creatureList[0]['choices'].append({
                'name': f'    {creature.hp} / {creature.maxHP} HP'
                + f'    Creature {creature.uid}'
            })

    selection = PyInquirer.prompt(creatureList, style=cliStyle)
    *_, selectedUID = selection['target'].split()
    matchedCreature = core.get_creature(int(selectedUID))

    return matchedCreature


def prompt_for_action(core, player, creature):
    itemList = [{
            'type': 'list',
            'message': 'Choose an item',
            'name': 'item',
            'choices': []
        }]
    questions = [{
            'type': 'list',
            'message': f'Choose Action for UID {creature.uid}',
            'name': 'action',
            'choices': []
        }]
    
    for action in core.globalActions:
        questions[0]['choices'].append({'name': action.name})
    if creature.availableActions:
        for action in creature.availableActions:
            questions[0]['choices'].append({'name': action.name})
    
    for i, item in enumerate(player.items):
        itemList[0]['choices'].append({'name': f'{i})    {item.name} ({item.get()})'})

    questions[0]['choices'].append({'name': 'Use Item'})
    questions[0]['choices'].append({'name': 'Quit'})

    selection = PyInquirer.prompt(questions, style=cliStyle)
    
    if selection['action'] == 'Use Item':
        selectedItem = PyInquirer.prompt(itemList, style=cliStyle)
        untrimmedIndex, itemName, _ = selectedItem['item'].split()
        selectionIndex = int(untrimmedIndex.strip(')'))
        if player.items[selectionIndex].name != itemName:
            raise TypeError('Item type does not match selected')
        return player.items[selectionIndex]
    
    for a in itertools.chain(core.globalActions, creature.availableActions):
        if a.name == selection['action']:
            return a
    
    if selection['action'] == 'Quit':
        exit(0)

