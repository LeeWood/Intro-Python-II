from item import Item

class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    #this lists all items in player inventory.
    def get_inventory(self): 
        output = ""
        i = 1
        for item in self.items:
            output += f"\n{i}. {item}"
            i += 1
        return output    
        # * maybe add incrementing numbers to this later
    
    #adds item to player item list
    def get_item(self, item):
        self.current_room.items.remove(item)
        self.items.append(item) 
        item.on_take() 

    #removes item to player item list
    def drop_item(self, item):
        self.current_room.items.append(item)
        self.items.remove(item)
        item.on_drop()        
            
    def __str__(self):
        return f'{self.name}, {self.current_room}'