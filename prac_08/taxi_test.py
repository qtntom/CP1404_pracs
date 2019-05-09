"""
prac 8 - walkthrough example
by Q.T
09May19
"""

from prac_08.taxi import Taxi

taxi1 = Taxi('Prius 1', 100, 1.23)
taxi1.drive(40)
print(taxi1)

taxi1.start_fare()
taxi1.drive(100)
print('{}, current fare {}$'.format(taxi1, taxi1.get_fare()))

taxi1.add_fuel(100)
taxi1.drive(40)
print('{}, current fare {}$'.format(taxi1, taxi1.get_fare()))
