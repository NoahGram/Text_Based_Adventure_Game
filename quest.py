class Quest:
    def __init__(self, id, name, description, experience_points_reward, gold_reward, item_reward, quest_completed_items):
        self.id = id
        self.name = name
        self.description = description
        self.experience_points_reward = experience_points_reward
        self.gold_reward = gold_reward
        self.item_reward = item_reward
        self.quest_completed = False
        self.quest_completed_items = quest_completed_items