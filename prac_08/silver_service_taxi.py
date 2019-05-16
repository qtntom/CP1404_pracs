from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """child class of Taxi, with price_per_km variable depending on fanciness, a new attribute"""
    flagfall = 4.5

    def __init__(self, fanciness=0.0, **kwargs):
        """initiate an instance of silver taxi based on parent taxi class with new attribute fanciness"""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """calculate fare like a normal taxi but with additional charge of flagfall"""
        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        """return string like a taxi but with flagfall added"""
        return super().__str__() + ' plus flagfall of ${:.2f}'.format(self.flagfall)
