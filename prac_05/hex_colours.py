"""
CP1404/CP5632 Practical
colour names in a dictionary
"""

COLOURS = {"BLUE": "#0000ff", "RED": "	#ff4500", "ORANGE": "#ffa500", "YELLOW": "#ffff00",
               "GREEN": "#9acd32", "BROWN": "#a52a2a", "BLACK": "#000000", 'WHITE': '#f8f8ff', 'PURPLE': '	#9370db', 'PINK': '#ff1493'}

colour_name = input('Please enter a colour: ').upper()
while colour_name != '':
    if colour_name in COLOURS:
        print('Code for {} is {}'.format(colour_name, COLOURS[colour_name]))
    else:
        print('Invalid color.')
    colour_name = input('Please enter a colour: ').upper()