from creature import Creature

class Player(Creature):
    def __init__(self, current_hit_points, maximum_hit_points, gold, experiencePoints, level):
        super().__init__(current_hit_points, maximum_hit_points)
        self.gold = gold
        self.experiencePoints = experiencePoints
        self.level = level
        self.inventory = []
        self.quests = []
        self.current_location = 1