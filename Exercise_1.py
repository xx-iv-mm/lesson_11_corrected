# Exercise 1

class Soda:
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        if self.name:
            return f'У вас газировка с {self.name} вкусом'
        else:
            return "У вас обычная газировка"