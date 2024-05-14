from creature import Creature

class Monster(Creature):
    def __init__(self, id, name, maximum_damage, experience_points_reward,
                 gold_reward, current_hit_points, maximum_hit_points):
        super().__init__(current_hit_points, maximum_hit_points)
        self.id = id
        self.name = name
        self.maximum_damage = maximum_damage
        self.experience_points_reward = experience_points_reward
        self.gold_reward = gold_reward
        self.loot_table = []