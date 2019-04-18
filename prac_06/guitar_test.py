'''
Test code for guitar class
'''

from prac_06.guitar import Guitar

guitar_1 = Guitar('Yamaha', 1920, 20000.542)
guitar_2 = Guitar('Honda', 1990, 2043.5)

print('{:8} get_age() - Expected {}. Got {}'.format(guitar_1.name, 99, guitar_1.get_age()))
print('{:8} get_age() - Expected 29. Got {}'.format(guitar_2.name, guitar_2.get_age()))

print('{:8} is_vintage() - Expected True. Got {}'.format(guitar_1.name, guitar_1.is_vintage()))
print('{:8} is_vintage() - Expected False. Got {}'.format(guitar_2.name, guitar_2.is_vintage()))
