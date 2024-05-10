class Location:
    def __init__(self, id, name, description, item_required_to_enter, quest_available_here, monster):
        self.id = id
        self.name = name
        self.description = description
        self.item_required_to_enter = item_required_to_enter
        self.quest_available_here = quest_available_here
        self.monster_living_here = monster
        self.location_to_north = None
        self.location_to_south = None
        self.location_to_east = None
        self.location_to_west = None

