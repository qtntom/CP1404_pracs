"""
Kivy GUI program to convert Miles to Kilometers
using Kivy language
By Q.T
May 19
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class MilesToKm(App):
    result = StringProperty()

    def build(self):
        self.title = 'Miles to Kilometers Converter'
        self.root = Builder.load_file('miles_to_km_converter.kv')
        return self.root

    def handle_conversion(self):
        self.result = self.root.ids.input_text.text
        # miles = float(self.root.ids.input_text.text)
        # print(miles)
        # self.result = miles * 1.60934


MilesToKm().run()
