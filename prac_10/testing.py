"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    strings = []
    for i in range(n):
        strings.append(s)
    return ' '.join(strings)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    # print(repeat_string('', 2))
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"


    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0, 'Car does not set fuel correctly'

    test_car = Car(fuel=10)
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 10, 'Car does not set fuel correctly'


run_tests()

doctest.testmod()


def change_phrase_to_sentence(phrase):
    """
    :param phrase:
    :return: phrase
    >>> change_phrase_to_sentence('hello')
    'Hello.'
    >>> change_phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> change_phrase_to_sentence('detect your tests')
    'Detect your tests.'
    """

    if phrase[-1] != '.':
        phrase += '.'
    return phrase[0].upper() + phrase[1:]
