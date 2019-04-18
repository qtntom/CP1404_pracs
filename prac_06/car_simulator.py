from prac_06.car import Car


def main():
    print("Let's drive!")
    car_name = input('Enter your car name: ')
    user_car = Car(car_name, 100)
    print_menu(user_car)

    user_choice = input('Enter your choice: ').upper()
    while user_choice != 'Q':
        if user_choice == 'D':
            pass
        elif user_choice == 'R':
            pass
        else:
            print('Invalid choice!\n')
            print_menu(user_car)
            user_choice = input('Enter your choice: ')

    print("Goodbye {}'s driver".format(user_car.name))


def print_menu(car):
    print(car)
    print('Menu:')
    print('d) drive')
    print('r) refuel')
    print('q) quit')


main()