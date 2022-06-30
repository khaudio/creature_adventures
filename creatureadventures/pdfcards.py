import fpdf
import pathlib
from action import *


def write_item_pdf(itemDeck):
    pass


def write_creature_pdf_from_deck(deck, filename, images):
    pdf = fpdf.FPDF(orientation='P', unit='in', format=(2.25, 3.5))
    pdf.set_title('Creature Adventures Creature Deck')
    pdf.set_margins(*(0.15 for _ in range(3)))
    pdf.set_auto_page_break(False, 0.15)
    pdf.set_font('Courier', size=11)
    design = None
    for item in pathlib.Path(images).iterdir():
        if 'creature_card_design' in item.name:
            design = item.as_posix()
    
    for card in deck:
        pdf.add_page()
        pdf.image(design, x=0.0, y=0.0, w=2.25, h=3.5)

        # Print creature name at top
        pdf.set_font('', size=11, style='B')
        name =  f'Creature'
        pdf.set_xy(0.15, 0.15)
        pdf.write(0.25, name)

        # Print creature HP to right of name
        pdf.set_font('', size=11, style='')
        maxHP = f'{card.maxHP} HP'
        pdf.set_xy(2.0 - pdf.get_string_width(maxHP), 0.15)
        pdf.write(0.25, maxHP)

        # Print creature tier beneath name
        pdf.set_font('', size=8, style='')
        pdf.set_xy(0.15, 0.32)
        pdf.write(0.25, card.tierName)

        # Print creature stats at bottom right
        pdf.set_font('', size=11, style='')
        stats = f'{card.attack} / {card.defense}'
        pdf.set_xy(2.0 - pdf.get_string_width(stats), 3.0)
        pdf.write(0.5, stats)

        # Print creature UID at bottom left
        pdf.set_font('', size=6, style='')
        pdf.set_xy(0.15, 3.0)
        pdf.write(0.5, f'UID #{card.uid}')

        # Print special action in body under creature image
        pdf.set_xy(0.15, 2.22)
        for action in card.availableActions:
            pdf.set_font('', size=9, style='B')
            pdf.write(0.15, f'{action.name}')
            pdf.set_font('', size=9, style='')
            pdf.write(0.15, f': {action.description}')
            if action != card.availableActions[-1]:
                pdf.write('\n')

    pdf.output(filename)


def write_item_pdf_from_deck(deck, filename, images):
    pdf = fpdf.FPDF(orientation='P', unit='in', format=(2.25, 3.5))
    pdf.set_title('Creature Adventures Item Deck')
    pdf.set_margins(*(0.15 for _ in range(3)))
    pdf.set_auto_page_break(False, 0.15)
    pdf.set_font('Courier', size=11)
    design = None
    for item in pathlib.Path(images).iterdir():
        if 'item_card_blank' in item.name:
            design = item.as_posix()
    
    for card in deck:
        pdf.add_page()
        pdf.image(design, x=0.0, y=0.0, w=2.25, h=3.5)

        # Print item name at top
        pdf.set_font('', size=11, style='B')
        pdf.set_xy(0.15, 0.15)
        pdf.write(0.25, item.name)

        # Print item tier beneath name
        pdf.set_font('', size=8, style='')
        pdf.set_xy(0.15, 0.32)
        pdf.write(0.25, card.tierName)

        # Print item UID at bottom left
        pdf.set_font('', size=6, style='')
        pdf.set_xy(0.15, 3.0)
        pdf.write(0.5, f'UID #{card.uid}')

        # Print item description in body under image
        pdf.set_xy(0.15, 2.22)
        pdf.set_font('', size=9, style='')
        pdf.write(0.15, f': {item.description}')

