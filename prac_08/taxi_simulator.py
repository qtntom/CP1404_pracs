from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def main():
    """Main function"""
    taxis = [Taxi('Prius', 100), SilverServiceTaxi(2, name='Limo', fuel=100),
             SilverServiceTaxi(4, name='Hummer', fuel=200)]

    print("Let's drive!")
    print_menu()
    menu_choice = input('>>>').lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            print_taxis(taxis)
        elif menu_choice == 'd':
            pass
        else:
            print('Invalid choice!')
        print_menu()
        menu_choice = input('>>>').lower()

def print_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print('{} - {}'.format(i, taxi))


def print_menu():
    print('q)uit, c)hoose taxi, d)rive')


main()
