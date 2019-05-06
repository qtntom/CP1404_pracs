"""
Extension work 3
Temperature converter program
By Q.T
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class TemperatureConverter(App):
    fahra = StringProperty()
    celcius = StringProperty()

    def build(self):
        self.title = 'Temperature conversion'
        self.root = Builder.load_file('extension_3.kv')
        return self.root

    def convert_to_fahra(self, celcius_text):
        try:
            self.fahra = str((float(celcius_text) * 9 / 5) + 32)
        except ValueError:
            self.celcius = '0'
            self.fahra = ''

    def convert_to_celcius(self):
        try:
            fahra = float(self.root.ids.fahra_value.text)
            self.celcius = str((fahra - 32) * 5 / 9)
        except ValueError:
            self.celcius = '0'
            self.fahra = ''

TemperatureConverter().run()