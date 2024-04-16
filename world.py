from item import Item
from location import Location
from monster import Monster
from potion import Potion
from quest import Quest
from weapon import Weapon
from loot_item import LootItem
from quest_completion_item import QuestCompletionItem

class World:
    Items = []
    Monsters = []
    Quests = []
    Locations = []

    ITEM_ID_RUSTY_SWORD = 1
    ITEM_ID_RAT_TAIL = 2
    ITEM_ID_PIECE_OF_FUR = 3
    ITEM_ID_SNAKE_FANG = 4
    ITEM_ID_SNAKESKIN = 5
    ITEM_ID_CLUB = 6
    ITEM_ID_HEALING_POTION = 7
    ITEM_ID_SPIDER_FANG = 8
    ITEM_ID_SPIDER_SILK = 9
    ITEM_ID_ADVENTURER_PASS = 10

    MONSTER_ID_RAT = 1
    MONSTER_ID_SNAKE = 2
    MONSTER_ID_GIANT_SPIDER = 3

    QUEST_ID_CLEAR_ALCHEMIST_GARDEN = 1
    QUEST_ID_CLEAR_FARMERS_FIELD = 2

    LOCATION_ID_HOME = 1
    LOCATION_ID_TOWN_SQUARE = 2
    LOCATION_ID_GUARD_POST = 3
    LOCATION_ID_ALCHEMIST_HUT = 4
    LOCATION_ID_ALCHEMISTS_GARDEN = 5
    LOCATION_ID_FARMHOUSE = 6
    LOCATION_ID_FARM_FIELD = 7
    LOCATION_ID_BRIDGE = 8
    LOCATION_ID_SPIDER_FIELD = 9

    @staticmethod
    def __init__():
        World.populate_items()
        World.populate_monsters()
        World.populate_quests()
        World.populate_locations()

    @staticmethod
    def populate_items():
        World.Items.append(Weapon(World.ITEM_ID_RUSTY_SWORD, "Rusty sword", "Rusty swords", 0, 5))
        World.Items.append(Item(World.ITEM_ID_RAT_TAIL, "Rat tail", "Rat tails"))
        World.Items.append(Item(World.ITEM_ID_PIECE_OF_FUR, "Piece of fur", "Pieces of fur"))
        World.Items.append(Item(World.ITEM_ID_SNAKE_FANG, "Snake fang", "Snake fangs"))
        World.Items.append(Item(World.ITEM_ID_SNAKESKIN, "Snakeskin", "Snakeskins"))
        World.Items.append(Weapon(World.ITEM_ID_CLUB, "Club", "Clubs", 3, 10))
        World.Items.append(Potion(World.ITEM_ID_HEALING_POTION, "Healing potion", "Healing potions", 5))
        World.Items.append(Item(World.ITEM_ID_SPIDER_FANG, "Spider fang", "Spider fangs"))
        World.Items.append(Item(World.ITEM_ID_SPIDER_SILK, "Spider silk", "Spider silks"))
        World.Items.append(Item(World.ITEM_ID_ADVENTURER_PASS, "Adventurer pass", "Adventurer passes"))

    @staticmethod
    def populate_monsters():
        rat = Monster(World.MONSTER_ID_RAT, "Rat", 5, 3, 10, 3, 3)
        rat.LootTable.append(LootItem(World.item_by_id(World.ITEM_ID_RAT_TAIL), 75, False))
        rat.LootTable.append(LootItem(World.item_by_id(World.ITEM_ID_PIECE_OF_FUR), 75, True))

        snake = Monster(World.MONSTER_ID_SNAKE, "Snake", 5, 3, 10, 3, 3)
        snake.LootTable.append(LootItem(World.item_by_id(World.ITEM_ID_SNAKE_FANG), 75, False))
        snake.LootTable.append(LootItem(World.item_by_id(World.ITEM_ID_SNAKESKIN), 75, True))

        giantSpider = Monster(World.MONSTER_ID_GIANT_SPIDER, "Giant spider", 20, 5, 40, 10, 10)
        giantSpider.LootTable.append(LootItem(World.item_by_id(World.ITEM_ID_SPIDER_FANG), 75, True))
        giantSpider.LootTable.append(LootItem(World.item_by_id(World.ITEM_ID_SPIDER_SILK), 25, False))

        World.Monsters.append(rat)
        World.Monsters.append(snake)
        World.Monsters.append(giantSpider)

    @staticmethod
    def populate_quests():
        clearAlchemistGarden = Quest(World.QUEST_ID_CLEAR_ALCHEMIST_GARDEN, "Clear the alchemist's garden", "Kill rats in the alchemist's garden and bring back 3 rat tails. You will receive a healing potion and 10 gold pieces.", 20, 10)
        clearAlchemistGarden.QuestCompletionItems.append(QuestCompletionItem(World.item_by_id(World.ITEM_ID_RAT_TAIL), 3))
        clearAlchemistGarden.RewardItem = World.item_by_id(World.ITEM_ID_HEALING_POTION)

        clearFarmersField = Quest(World.QUEST_ID_CLEAR_FARMERS_FIELD, "Clear the farmer's field", "Kill snakes in the farmer's field and bring back 3 snake fangs. You will receive an adventurer's pass and 20 gold pieces.", 20, 20)
        clearFarmersField.QuestCompletionItems.append(QuestCompletionItem(World.item_by_id(World.ITEM_ID_SNAKE_FANG), 3))
        clearFarmersField.RewardItem = World.item_by_id(World.ITEM_ID_ADVENTURER_PASS)

        World.Quests.append(clearAlchemistGarden)
        World.Quests.append(clearFarmersField)

    @staticmethod
    def populate_locations():
        home = Location(World.LOCATION_ID_HOME, "Home", "Your house. You really need to clean up the place.")

        townSquare = Location(World.LOCATION_ID_TOWN_SQUARE, "Town square", "You see a fountain.")

        alchemistHut = Location(World.LOCATION_ID_ALCHEMIST_HUT, "Alchemist's hut", "There are many strange plants on the shelves.")
        alchemistHut.QuestAvailableHere = World.quest_by_id(World.QUEST_ID_CLEAR_ALCHEMIST_GARDEN)

        alchemistsGarden = Location(World.LOCATION_ID_ALCHEMISTS_GARDEN, "Alchemist's garden", "Many plants are growing here.")
        alchemistsGarden.MonsterLivingHere = World.monster_by_id(World.MONSTER_ID_RAT)

        farmhouse = Location(World.LOCATION_ID_FARMHOUSE, "Farmhouse", "There is a small farmhouse, with a farmer in front.")
        farmhouse.QuestAvailableHere = World.quest_by_id(World.QUEST_ID_CLEAR_FARMERS_FIELD)

        farmersField = Location(World.LOCATION_ID_FARM_FIELD, "Farmer's field", "You see rows of vegetables growing here.")
        farmersField.MonsterLivingHere = World.monster_by_id(World.MONSTER_ID_SNAKE)

        guardPost = Location(World.LOCATION_ID_GUARD_POST, "Guard post", "There is a large, tough-looking guard here.", World.item_by_id(World.ITEM_ID_ADVENTURER_PASS))

        bridge = Location(World.LOCATION_ID_BRIDGE, "Bridge", "A stone bridge crosses a wide river.")

        spiderField = Location(World.LOCATION_ID_SPIDER_FIELD, "Forest", "You see spider webs covering covering the trees in this forest.")
        spiderField.MonsterLivingHere = World.monster_by_id(World.MONSTER_ID_GIANT_SPIDER)

        home.LocationToNorth = townSquare

        townSquare.LocationToNorth = alchemistHut
        townSquare.LocationToSouth = home
        townSquare.LocationToEast = guardPost
        townSquare.LocationToWest = farmhouse

        farmhouse.LocationToEast = townSquare
        farmhouse.LocationToWest = farmersField

        farmersField.LocationToEast = farmhouse

        alchemistHut.LocationToSouth = townSquare
        alchemistHut.LocationToNorth = alchemistsGarden

        alchemistsGarden.LocationToSouth = alchemistHut

        guardPost.LocationToEast = bridge
        guardPost.LocationToWest = townSquare

        bridge.LocationToWest = guardPost
        bridge.LocationToEast = spiderField

        spiderField.LocationToWest = bridge

        World.Locations.append(home)
        World.Locations.append(townSquare)
        World.Locations.append(guardPost)
        World.Locations.append(alchemistHut)
        World.Locations.append(alchemistsGarden)
        World.Locations.append(farmhouse)
        World.Locations.append(farmersField)
        World.Locations.append(bridge)
        World.Locations.append(spiderField)

    @staticmethod
    def item_by_id(id):
        for item in World.Items:
            if item.ID == id:
                return item
        return None

    @staticmethod
    def monster_by_id(id):
        for monster in World.Monsters:
            if monster.ID == id:
                return monster
        return None

    @staticmethod
    def quest_by_id(id):
        for quest in World.Quests:
            if quest.ID == id:
                return quest
        return None

    @staticmethod
    def location_by_id(id):
        for location in World.Locations:
            if location.ID == id:
                return location
        return None