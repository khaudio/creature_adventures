import fpdf
from action import *


def write_creature_pdf_from_deck(deck, filename='../build/creature_cards.pdf'):
    pdf = fpdf.FPDF(orientation='P', unit='in', format=(2.25, 3.5))
    pdf.set_title('Creature Adventures Creature Deck')
    pdf.set_margins(*(0.15 for _ in range(3)))
    pdf.set_auto_page_break(False, 0.15)
    pdf.set_font('Courier', size=11)

    for card in deck:
        pdf.add_page()
        pdf.image(
                '../images/creature_card_design.jpg',
                x=0.0,
                y=0.0,
                w=2.25,
                h=3.5
            )

        # Print creature name at top
        pdf.set_font('', size=11, style='B')
        name =  f'Creature UID {card.uid}'
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

