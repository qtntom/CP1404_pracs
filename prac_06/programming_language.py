'''
Programming language class
'''


class ProgrammingLanguage:
    def __init__(self, name='', typing='Static', reflection=True, year=1990):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == 'Dynamic'

    def __str__(self):
        return '{}, {} Typing, Reflection={}, First appeared in {}'.format(self.name, self.typing, self.reflection,
                                                                           self.year)