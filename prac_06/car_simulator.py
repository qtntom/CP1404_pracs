"""
Car simulator using Car class
"""
from prac_06.car import Car


def main():
    print("Let's drive!")
    car_name = input('Enter your car name: ')
    user_car = Car(car_name, 100)
    print_menu(user_car)

    user_choice = input('Enter your choice: ').upper()
    while user_choice != 'Q':
        if user_choice == 'D':
            # TODO: function to drive car
            if user_car.fuel == 0:
                print("The car has no fuel left. Please select 'r' to refuel.")
            else:
                drive_distance = get_int_above_zero('How many units of fuel do you want to add to the car? ')
                user_car.drive(drive_distance)
            print_menu(user_car)
            user_choice = input('Enter your choice: ').upper()
        elif user_choice == 'R':
            # TODO: function to refuel
            refuel_amount = get_int_above_zero('How many units of fuel do you want to add to the car? ')
            user_car.add_fuel(refuel_amount)
            print_menu(user_car)
            user_choice = input('Enter your choice: ').upper()
        else:
            print('Invalid choice!\n')
            print_menu(user_car)
            user_choice = input('Enter your choice: ').upper()

    print("Goodbye {}'s driver".format(user_car.name))


def get_int_above_zero(input_question):
    valid_input = False
    while not valid_input:
        try:
            input_value = int(input(input_question))
            if input_value < 0:
                print('Input must be >= 0')
            else:
                valid_input = True
        except ValueError:
            print('Invalid input!')
    return input_value


def print_menu(car):
    print(car)
    print('Menu:')
    print('d) drive')
    print('r) refuel')
    print('q) quit')


main()
