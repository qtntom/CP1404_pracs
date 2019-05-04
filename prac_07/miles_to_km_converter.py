"""
Kivy GUI program to convert Miles to Kilometers
using Kivy language
By Q.T
May 19
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

CONVERSION_RATE = 1.60934


class MilesToKm(App):
    result = StringProperty()

    def build(self):
        self.title = 'Miles to Kilometers Converter'
        self.root = Builder.load_file('miles_to_km_converter.kv')
        return self.root

    def handle_conversion(self):
        try:
            miles = float(self.root.ids.input_text.text)
            self.result = str(miles * CONVERSION_RATE)
        except ValueError:
            self.root.ids.input_text.text = '0'
            self.result = '0'

    def handle_increment(self, value):
        try:
            self.root.ids.input_text.text = str(float(self.root.ids.input_text.text) + value)
        except ValueError:
            self.root.ids.input_text.text = str(0 + value)


MilesToKm().run()
