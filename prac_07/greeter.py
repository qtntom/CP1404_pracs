from kivy.app import App
from kivy.lang import Builder


class Greeter(App):
    SIZE_MARGIN = .3

    def build(self):
        self.title = "Greeter"
        self.root = Builder.load_file('greeter.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = 'Hello ' + self.root.ids.input_name.text

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


Greeter().run()
