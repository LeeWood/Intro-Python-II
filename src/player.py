class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def get_items(self):
        for item in self.items:
            return item
        # * maybe add incrementing numbers to this later

    def __str__(self):
        return f'{self.name}, {self.current_room}'