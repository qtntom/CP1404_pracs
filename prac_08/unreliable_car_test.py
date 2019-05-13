from prac_08.unreliable_car import UnreliableCar

bad_car = UnreliableCar()
bad_car.reliability = 30
bad_car.fuel = 500
bad_car.name = 'Satan'

good_car = UnreliableCar(fuel=500, reliability=80)
good_car.name = 'God'

for i in range(5):
    bad_car.drive(100)
print(bad_car, end='\n')

for i in range(5):
    good_car.drive(100)
print(good_car)
