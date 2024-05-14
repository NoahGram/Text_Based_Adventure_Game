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
        
    def add_item_to_inventory(self, item):
        self.inventory.append(item)