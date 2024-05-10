class Location:
    def __init__(self, id, name, description, item_required_to_enter, quest_available_here, monster, location_to_north=None, location_to_east=None, location_to_south=None, location_to_west=None):
        self.id = id
        self.name = name
        self.description = description
        self.item_required_to_enter = item_required_to_enter
        self.quest_available_here = quest_available_here
        self.monster_living_here = monster
        ## Not needed i think :D
        self.location_to_north = location_to_north
        self.location_to_south = location_to_south
        self.location_to_east = location_to_east
        self.location_to_west = location_to_west

