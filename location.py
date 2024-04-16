class Location:
    def __init__(self, id, name, description, item_required_to_enter=None, quest_available_here=None, monster=None):
        self.id = id
        self.name = name
        self.description = description
        self.item_required_to_enter = item_required_to_enter
        self.quest_available_here = quest_available_here
        self.monster = monster

