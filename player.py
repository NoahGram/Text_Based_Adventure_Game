from creature import Creature
from location import Location
from world import World

class Player(Creature):
    def __init__(self, current_hit_points, maximum_hit_points, gold, experience_points, level):
        super().__init__(current_hit_points, maximum_hit_points)
        self.gold = gold
        self.experience_points = experience_points
        self.level = level
        self.inventory = []
        self.quests = []
        self.current_location = World.location_by_id(World.LOCATION_ID_HOME)
        
    def add_item_to_inventory(self, item_to_add):
        # Check if item already exists in inventory
        for inventory_item in self.inventory:
            if inventory_item.details == item_to_add.details:
                # Item exists, increase quantity
                inventory_item.quantity += item_to_add.quantity
                break
        else:
            # Item doesn't exist, add to inventory
            self.inventory.append(item_to_add)