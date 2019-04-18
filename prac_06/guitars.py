'''
Client code, playing with the guitars...class
'''

from prac_06.guitar import Guitar

guitars = []
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print('My guitars!')

name = input('Name: ')
while name != '':
    year = int(input('Year: '))
    cost = float(input('Cost: '))
    guitars.append(Guitar(name, year, cost))
    print('{} ({}) : ${:,.2f} added'.format(name, year, cost))
    name = input('Name: ')

print('\n.....snip.....\n')
print('These are my guitars:')
for i, guitar in enumerate(guitars):
    vintage_string = '(vintage)' if guitar.is_vintage() else ''
    print("Guitar {}: {:>15} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))
