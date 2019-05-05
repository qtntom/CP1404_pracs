"""
Prac 7
Simple Dynamic widgets program
By Q.T
"""

from kivy.lang import Builder
from kivy.app import App
# from kivy.app import StringProperty
from kivy.uix.label import Label


class DynamicWidgetsPrac(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.words = ['abc', '123', 'def', '456']

    def build(self):
        self.title = 'Practical exercise on Dynamic widgets'
        self.root = Builder.load_file('dynamic_widgets_prac.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for word in self.words:
            temp_label = Label(text=word, color=(1, 0, 0, 1))
            self.root.ids.labels_field.add_widget(temp_label)

# TODO: how to create white labels?
DynamicWidgetsPrac().run()
