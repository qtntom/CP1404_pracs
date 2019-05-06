"""
Extension 4 exercise
dynamically generated GUI with file input
By Q.T
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

FILENAME = 'names_ages'


class DynamicGUI(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names_ages = self.extract_file_data()

    def build(self):
        self.root = Builder.load_file('extension_4.kv')
        self.add_widgets()
        return self.root

    def add_widgets(self):
        for name in self.names_ages:
            temp_button = Button(text=name, background_color=(0, 1, 1, 1))
            temp_button.bind(on_release=self.handle_press)
            self.root.ids.buttons_field.add_widget(temp_button)

    def handle_press(self, instance):
        self.root.ids.output_text.text = self.names_ages[instance.text]

    def extract_file_data(self):
        work_file = open(FILENAME)
        names_ages = {}
        for line in work_file:
            name_age = line.strip().split(',')
            names_ages[name_age[0]] = name_age[1]
        work_file.close()
        return names_ages


DynamicGUI().run()
