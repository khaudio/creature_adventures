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


def prompt_for_action(core, creature):
    questions = [
        {
                'type': 'list',
                'message': f'Choose Action for UID {creature.uid}',
                'name': 'action',
                'choices': []
            }
        ]
    
    for action in core.globalActions:
        questions[0]['choices'].append({'name': action.name})
    if creature.availableActions:
        for action in creature.availableActions:
            questions[0]['choices'].append({'name': action.name})
    
    questions[0]['choices'].append({'name': 'Quit'})

    selection = PyInquirer.prompt(questions, style=cliStyle)
    
    for a in itertools.chain(core.globalActions, creature.availableActions):
        if a.name == selection['action']:
            return a
    
    if selection['action'] == 'Quit':
        exit(0)

