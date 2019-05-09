"""
CP1404 Prac 7 - Extension 2
Simple GUI
By Q.T
"""

from kivy.app import App
from kivy.lang import Builder


class Grader(App):
    SIZE_MARGIN = .3

    def build(self):
        self.title = "Grade classifier"
        self.root = Builder.load_file('extension_2.kv')
        return self.root

    def handle_greet(self):
        try:
            grade = int(self.root.ids.input_grade.text)
            if grade < 0:
                self.root.ids.output_label.text = 'Invalid Grade!'
            # if grade < 50:
            #     self.root.ids.output_label.text = 'Fail!'
            # else:
            #     self.root.ids.output_label.text = 'Pass.'
            elif grade < 50:
                self.root.ids.output_label.text = 'Fail!'
            elif grade <65:
                self.root.ids.output_label.text = 'Pass!'
            elif grade < 75:
                self.root.ids.output_label.text = 'Credit!'
            elif grade < 85:
                self.root.ids.output_label.text = 'Distinction!'
            elif grade <= 100:
                self.root.ids.output_label.text = 'HD!'
            else:
                self.root.ids.output_label.text = 'Invalid grade!'

        except ValueError:
            self.root.ids.output_label.text = 'Invalid grade!'

    def handle_clear(self):
        self.root.ids.input_grade.text = ''
        self.root.ids.output_label.text = ''


Grader().run()
