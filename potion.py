from item import Item

class Potion(Item):
    def __init__(self, id, name, name_plural, amount_to_heal):
        super().__init__(id, name, name_plural)
        self.amount_to_heal = amount_to_heal