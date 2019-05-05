"""
Extension work 3
Temperature converter program
By Q.T
"""

from kivy.app import App
from kivy.lang import Builder


class TemperatureConverter(App):
    def build(self):
        self.title = 'Temperature conversion'
        self.root = Builder.load_file('extension_3.kv')
        return self.root

    def convert_to_fahra(self, celcius):
        return celcius * 9 / 5 + 32
