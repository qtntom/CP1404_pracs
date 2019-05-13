from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """child class of Car that has reliability rate"""

    def __init__(self, reliability=0, **kwargs):
        """initialize a UnreliableCar instance, based on parent Car class and its own attribute: reliability"""
        super().__init__(self, **kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """return driven distance, depends on a randomly generated number compared to reliability"""
        if randint(0, 100) < self.reliability:
            super().drive(distance)
        else:
            super().drive(0)
