"""
Extension 4 exercise
dynamically generated GUI with file input
By Q.T
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

FILENAME = 'names_ages'

def main():
    names_ages = extract_file_data()
    print(names_ages)

def extract_file_data():
    work_file = open(FILENAME)
    names_ages = {}
    for line in work_file:
        name_age = line.strip().split(',')
        names_ages[name_age[0]] = int(name_age[1])
    return names_ages

main()