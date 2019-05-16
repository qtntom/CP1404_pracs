"""
Taxi simulator using Taxi and SilverServiceTaxi class
By Q.T
"""

from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def main():
    """Main function"""
    taxis = [Taxi('Prius', 100), SilverServiceTaxi(2, name='Limo', fuel=100),
             SilverServiceTaxi(4, name='Hummer', fuel=200)]
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    print_menu()

    # Get menu choice loop
    menu_choice = input('>>>').lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            # choose a taxi and start fare on that taxi
            print('Taxis available:')
            print_taxis(taxis)
            current_taxi = taxis[get_taxi_number(len(taxis))]
            current_taxi.start_fare()
            print('Bill to date: ${:.2f}'.format(total_bill))
        elif menu_choice == 'd':
            # drive the chosen taxi and print out trip cost and total cost
            distance = int(input('Drive how far? '))
            current_taxi.drive(distance)
            cost = current_taxi.get_fare()
            print('Your {} trip cost you ${:.2f}'.format(current_taxi.name, cost))
            total_bill += cost
            print('Bill to date: ${:.2f}'.format(total_bill))
        else:
            print('Invalid choice!')
        print_menu()
        menu_choice = input('>>>').lower()
    # Finish off with trip summary and taxis remaining states
    print('Total trip cost: ${:.2f}'.format(total_bill))
    print('Taxis are now:')
    print_taxis(taxis)


def print_taxis(taxis):
    """Print all taxis in the list with index number at front"""
    for i, taxi in enumerate(taxis):
        print('{} - {}'.format(i, taxi))


def print_menu():
    """Print menu choices"""
    print('q)uit, c)hoose taxi, d)rive')


def get_taxi_number(max_number):
    """Get valid taxi number"""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input('Choose taxi: '))
            if number < 0:
                print('Taxi number must be greater or equal zero')
            elif number > (max_number - 1):
                print('Number is too high.')
            else:
                return number
        except ValueError:
            print('Invalid number!')


main()
