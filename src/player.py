class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    #this lists all items in player inventory.
    def get_inventory(self): 
        for item in self.items:
            return item
        # * maybe add incrementing numbers to this later

    def get_item(self, item):
        from item import Item
        
        if item == item.name:
            self.items.append(Item(item.name, item.description)) 
            item.on_take()   

    def __str__(self):
        return f'{self.name}, {self.current_room}'