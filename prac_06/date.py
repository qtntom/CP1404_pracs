"""
Date class
"""

class Date:
    def __init__(self, day=1, month=1, year=1):
        self.day = day%30
        self.month = month % 12
        self.year = year

    def __str__(self):
        return '{}/{}/{}'.format(self.day, self.month, self.year)

    def add_days(self, n):
        self.day += n