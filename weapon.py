from item import Item

class Weapon(Item):
    def __init__(self, id, name, name_plural, minimum_damage, maximum_damage):
        super().__init__(id, name, name_plural)
        self.minimum_damage = minimum_damage
        self.maximum_damage = maximum_damage