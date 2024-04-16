from creature import Creature

class Monster(Creature):
    def __init__(self, current_hit_points, maximum_hit_points, id, name, 
                 maximum_damage, reward_experience_points, reward_gold, loot_table):
        super().__init__(current_hit_points, maximum_hit_points)
        self.id = id
        self.name = name
        self.maximum_damage = maximum_damage
        self.reward_experience_points = reward_experience_points
        self.reward_gold = reward_gold
        self.loot_table = loot_table