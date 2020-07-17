class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def __str__(self):
        if len(self.items) < 0:
            return f'You are now in the {self.name}. {self.description}. You look around and see {self.items}'
        else:
            return f'You are now in the {self.name}. {self.description} You notice nothing else in this area.'


        