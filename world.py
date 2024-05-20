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
    ITEM_ID_LIQUID_DIVINIUM = 11
    ITEM_ID_IRON_SWORD = 12
    ITEM_ID_DRAGON_SCALE = 13
    ITEM_ID_WIZARD_STAFF = 14
    ITEM_ID_MAGIC_POTION = 15
    ITEM_ID_GOBLIN_EAR = 16
    ITEM_ID_GOLD_COIN = 17
    ITEM_ID_WOODEN_SHIELD = 18
    ITEM_ID_STEEL_SWORD = 19
    ITEM_ID_BOW_AND_ARROW = 20
    ITEM_ID_BATTLE_AXE = 21
    ITEM_ID_DAGGER = 22
    ITEM_ID_MACE = 23
    ITEM_ID_CROSSBOW = 24
    ITEM_ID_WAR_HAMMER = 25
    ITEM_ID_SPEAR = 26
    ITEM_ID_MAGIC_WAND = 27
    ITEM_ID_STAMINA_POTION = 28
    ITEM_ID_MANA_POTION = 29
    ITEM_ID_ANTIDOTE = 30
    ITEM_ID_STRENGTH_POTION = 31
    ITEM_ID_SPEED_POTION = 32
    ITEM_ID_INVISIBILITY_POTION = 33
    ITEM_ID_FIRE_RESISTANCE_POTION = 34
    ITEM_ID_WATER_BREATHING_POTION = 35
    ITEM_ID_NIGHT_VISION_POTION = 36
    ITEM_ID_LUCK_POTION = 37
    ITEM_ID_TORCH = 38
    ITEM_ID_ROPE = 39
    ITEM_ID_LOCKPICK_SET = 40
    ITEM_ID_MAP_OF_THE_KINGDOM = 41
    ITEM_ID_COMPASS = 42
    ITEM_ID_MAGIC_CRYSTAL = 43
    ITEM_ID_ANCIENT_COIN = 44
    ITEM_ID_HERBS = 45
    ITEM_ID_SPELL_BOOK = 46
    ITEM_ID_ENCHANTED_AMULET = 47
    ITEM_ID_TRAVELER_CLOAK = 48
    ITEM_ID_MAGIC_SCROLL = 49
    ITEM_ID_DRAGON_EGG = 50
    ITEM_ID_PHOENIX_FEATHER = 51
    ITEM_ID_RUNESTONE = 52
    ITEM_ID_ELVEN_BREAD = 53
    ITEM_ID_MYSTIC_ORB = 54
    ITEM_ID_GOLEM_HEART = 55
    ITEM_ID_ELEMENTAL_STONE = 56
    ITEM_ID_WIZARD_HAT = 57
    ITEM_ID_HEALING_HERB = 58
    ITEM_ID_SILVER_KEY = 59
    ITEM_ID_GOLDEN_APPLE = 60
    ITEM_ID_PIRATE_TREASURE_MAP = 61
    ITEM_ID_WYRM_SCALE = 62
    ITEM_ID_FAIRY_DUST = 63
    ITEM_ID_MERMAID_TEAR = 64
    ITEM_ID_SKELETON_KEY = 65
    ITEM_ID_ANCIENT_RELIC = 66
    ITEM_ID_TREASURE_CHEST = 67


    MONSTER_ID_RAT = 1
    MONSTER_ID_SNAKE = 2
    MONSTER_ID_GIANT_SPIDER = 3
    MONSTER_ID_GOBLIN = 4
    MONSTER_ID_DRAGON = 5

    QUEST_ID_CLEAR_ALCHEMIST_GARDEN = 1
    QUEST_ID_CLEAR_FARMERS_FIELD = 2
    QUEST_ID_SLAY_GOBLIN_LEADER = 3
    QUEST_ID_RETRIEVE_DRAGON_SCALE = 4

    LOCATION_ID_HOME = 1
    LOCATION_ID_TOWN_SQUARE = 2
    LOCATION_ID_GUARD_POST = 3
    LOCATION_ID_ALCHEMIST_HUT = 4
    LOCATION_ID_ALCHEMISTS_GARDEN = 5
    LOCATION_ID_FARMHOUSE = 6
    LOCATION_ID_FARM_FIELD = 7
    LOCATION_ID_BRIDGE = 8
    LOCATION_ID_SPIDER_FIELD = 9
    LOCATION_ID_DARK_FOREST = 10
    LOCATION_ID_GOBLIN_CAVE = 11
    LOCATION_ID_DRAGON_LAIR = 12
    LOCATION_ID_MAGIC_SHOP = 13

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
        World.Items.append(Potion(World.ITEM_ID_LIQUID_DIVINIUM, "Liquid Divinium", "Liquid Diviniums", 50))
        World.Items.append(Weapon(World.ITEM_ID_IRON_SWORD, "Iron sword", "Iron swords", 10, 20))
        World.Items.append(Item(World.ITEM_ID_DRAGON_SCALE, "Dragon scale", "Dragon scales"))
        World.Items.append(Weapon(World.ITEM_ID_WIZARD_STAFF, "Wizard staff", "Wizard staffs", 15, 25))
        World.Items.append(Potion(World.ITEM_ID_MAGIC_POTION, "Magic potion", "Magic potions", 10))
        World.Items.append(Item(World.ITEM_ID_GOBLIN_EAR, "Goblin ear", "Goblin ears"))
        World.Items.append(Item(World.ITEM_ID_GOLD_COIN, "Gold coin", "Gold coins"))
        World.Items.append(Weapon(World.ITEM_ID_WOODEN_SHIELD, "Wooden Shield", "Wooden Shields", 0, 3))
        World.Items.append(Weapon(World.ITEM_ID_STEEL_SWORD, "Steel Sword", "Steel Swords", 10, 15))
        World.Items.append(Weapon(World.ITEM_ID_BOW_AND_ARROW, "Bow and Arrow", "Bows and Arrows", 5, 12))
        World.Items.append(Weapon(World.ITEM_ID_BATTLE_AXE, "Battle Axe", "Battle Axes", 15, 25))
        World.Items.append(Weapon(World.ITEM_ID_DAGGER, "Dagger", "Daggers", 2, 8))
        World.Items.append(Weapon(World.ITEM_ID_MACE, "Mace", "Maces", 8, 18))
        World.Items.append(Weapon(World.ITEM_ID_CROSSBOW, "Crossbow", "Crossbows", 12, 20))
        World.Items.append(Weapon(World.ITEM_ID_WAR_HAMMER, "War Hammer", "War Hammers", 20, 30))
        World.Items.append(Weapon(World.ITEM_ID_SPEAR, "Spear", "Spears", 7, 14))
        World.Items.append(Weapon(World.ITEM_ID_MAGIC_WAND, "Magic Wand", "Magic Wands", 3, 10))
        World.Items.append(Potion(World.ITEM_ID_STAMINA_POTION, "Stamina Potion", "Stamina Potions", 5))
        World.Items.append(Potion(World.ITEM_ID_MANA_POTION, "Mana Potion", "Mana Potions", 5))
        World.Items.append(Potion(World.ITEM_ID_ANTIDOTE, "Antidote", "Antidotes", 3))
        World.Items.append(Potion(World.ITEM_ID_STRENGTH_POTION, "Strength Potion", "Strength Potions", 10))
        World.Items.append(Potion(World.ITEM_ID_SPEED_POTION, "Speed Potion", "Speed Potions", 10))
        World.Items.append(Potion(World.ITEM_ID_INVISIBILITY_POTION, "Invisibility Potion", "Invisibility Potions", 20))
        World.Items.append(Potion(World.ITEM_ID_FIRE_RESISTANCE_POTION, "Fire Resistance Potion", "Fire Resistance Potions", 8))
        World.Items.append(Potion(World.ITEM_ID_WATER_BREATHING_POTION, "Water Breathing Potion", "Water Breathing Potions", 12))
        World.Items.append(Potion(World.ITEM_ID_NIGHT_VISION_POTION, "Night Vision Potion", "Night Vision Potions", 6))
        World.Items.append(Potion(World.ITEM_ID_LUCK_POTION, "Luck Potion", "Luck Potions", 15))
        World.Items.append(Item(World.ITEM_ID_TORCH, "Torch", "Torches"))
        World.Items.append(Item(World.ITEM_ID_ROPE, "Rope", "Ropes"))
        World.Items.append(Item(World.ITEM_ID_LOCKPICK_SET, "Lockpick Set", "Lockpick Sets"))
        World.Items.append(Item(World.ITEM_ID_MAP_OF_THE_KINGDOM, "Map of the Kingdom", "Maps of the Kingdom"))
        World.Items.append(Item(World.ITEM_ID_COMPASS, "Compass", "Compasses"))
        World.Items.append(Item(World.ITEM_ID_MAGIC_CRYSTAL, "Magic Crystal", "Magic Crystals"))
        World.Items.append(Item(World.ITEM_ID_ANCIENT_COIN, "Ancient Coin", "Ancient Coins"))
        World.Items.append(Item(World.ITEM_ID_HERBS, "Herbs", "Herbs"))
        World.Items.append(Item(World.ITEM_ID_SPELL_BOOK, "Spell Book", "Spell Books"))
        World.Items.append(Item(World.ITEM_ID_ENCHANTED_AMULET, "Enchanted Amulet", "Enchanted Amulets"))
        World.Items.append(Item(World.ITEM_ID_TRAVELER_CLOAK, "Traveler's Cloak", "Traveler's Cloaks"))
        World.Items.append(Item(World.ITEM_ID_MAGIC_SCROLL, "Magic Scroll", "Magic Scrolls"))
        World.Items.append(Item(World.ITEM_ID_DRAGON_EGG, "Dragon Egg", "Dragon Eggs"))
        World.Items.append(Item(World.ITEM_ID_PHOENIX_FEATHER, "Phoenix Feather", "Phoenix Feathers"))
        World.Items.append(Item(World.ITEM_ID_RUNESTONE, "Runestone", "Runestones"))
        World.Items.append(Item(World.ITEM_ID_ELVEN_BREAD, "Elven Bread", "Elven Breads"))
        World.Items.append(Item(World.ITEM_ID_MYSTIC_ORB, "Mystic Orb", "Mystic Orbs"))
        World.Items.append(Item(World.ITEM_ID_GOLEM_HEART, "Golem Heart", "Golem Hearts"))
        World.Items.append(Item(World.ITEM_ID_ELEMENTAL_STONE, "Elemental Stone", "Elemental Stones"))
        World.Items.append(Item(World.ITEM_ID_WIZARD_HAT, "Wizard Hat", "Wizard Hats"))
        World.Items.append(Item(World.ITEM_ID_HEALING_HERB, "Healing Herb", "Healing Herbs"))
        World.Items.append(Item(World.ITEM_ID_SILVER_KEY, "Silver Key", "Silver Keys"))
        World.Items.append(Item(World.ITEM_ID_GOLDEN_APPLE, "Golden Apple", "Golden Apples"))
        World.Items.append(Item(World.ITEM_ID_PIRATE_TREASURE_MAP, "Pirate Treasure Map", "Pirate Treasure Maps"))
        World.Items.append(Item(World.ITEM_ID_WYRM_SCALE, "Wyrm Scale", "Wyrm Scales"))
        World.Items.append(Item(World.ITEM_ID_FAIRY_DUST, "Fairy Dust", "Fairy Dusts"))
        World.Items.append(Item(World.ITEM_ID_MERMAID_TEAR, "Mermaid Tear", "Mermaid Tears"))
        World.Items.append(Item(World.ITEM_ID_SKELETON_KEY, "Skeleton Key", "Skeleton"))
        World.Items.append(Item(World.ITEM_ID_ANCIENT_RELIC, "Ancient Relic", "Ancient Relics"))
        World.Items.append(Item(World.ITEM_ID_TREASURE_CHEST, "Treasure Chest", "Treasure Chests"))


    @staticmethod
    def populate_monsters():
        rat = Monster(World.MONSTER_ID_RAT, "Rat", 5, 3, 10, 3, 3)
        rat.loot_table.append(LootItem(World.item_by_id(World.ITEM_ID_RAT_TAIL), 75, False))
        rat.loot_table.append(LootItem(World.item_by_id(World.ITEM_ID_PIECE_OF_FUR), 75, True))

        snake = Monster(World.MONSTER_ID_SNAKE, "Snake", 5, 3, 10, 3, 3)
        snake.loot_table.append(LootItem(World.item_by_id(World.ITEM_ID_SNAKE_FANG), 75, False))
        snake.loot_table.append(LootItem(World.item_by_id(World.ITEM_ID_SNAKESKIN), 75, True))

        giantSpider = Monster(World.MONSTER_ID_GIANT_SPIDER, "Giant spider", 20, 5, 40, 10, 10)
        giantSpider.loot_table.append(LootItem(World.item_by_id(World.ITEM_ID_SPIDER_FANG), 75, True))
        giantSpider.loot_table.append(LootItem(World.item_by_id(World.ITEM_ID_SPIDER_SILK), 25, False))

        goblin = Monster(World.MONSTER_ID_GOBLIN, "Goblin", 15, 7, 30, 5, 5)
        goblin.loot_table.append(LootItem(World.item_by_id(World.ITEM_ID_GOBLIN_EAR), 75, True))
        goblin.loot_table.append(LootItem(World.item_by_id(World.ITEM_ID_GOLD_COIN), 50, False))

        dragon = Monster(World.MONSTER_ID_DRAGON, "Dragon", 100, 20, 200, 50, 50)
        dragon.loot_table.append(LootItem(World.item_by_id(World.ITEM_ID_DRAGON_SCALE), 100, True))

        World.Monsters.append(rat)
        World.Monsters.append(snake)
        World.Monsters.append(giantSpider)
        World.Monsters.append(goblin)
        World.Monsters.append(dragon)

    @staticmethod
    def populate_quests():
        clearAlchemistGarden = Quest(
            World.QUEST_ID_CLEAR_ALCHEMIST_GARDEN, 
            "Clear the alchemist's garden", 
            "Kill rats in the alchemist's garden and bring back 3 rat tails. You will receive a healing potion and 10 gold pieces.", 
            20, 
            10,
            World.item_by_id(World.ITEM_ID_HEALING_POTION),  # item_reward
            [QuestCompletionItem(World.item_by_id(World.ITEM_ID_RAT_TAIL), 3)]  # quest_completed_items
        )

        clearFarmersField = Quest(
            World.QUEST_ID_CLEAR_FARMERS_FIELD, 
            "Clear the farmer's field", 
            "Kill snakes in the farmer's field and bring back 3 snake fangs. You will receive an adventurer's pass and 20 gold pieces.", 
            20, 
            20,
            World.item_by_id(World.ITEM_ID_ADVENTURER_PASS),  # item_reward
            [QuestCompletionItem(World.item_by_id(World.ITEM_ID_SNAKE_FANG), 3)]  # quest_completed_items
        )

        slayGoblinLeader = Quest(
            World.QUEST_ID_SLAY_GOBLIN_LEADER,
            "Slay the Goblin Leader",
            "Defeat the Goblin Leader in the Dark Forest and bring back his ear. You will receive a wizard staff and 50 gold pieces.",
            100,
            50,
            World.item_by_id(World.ITEM_ID_WIZARD_STAFF),  # item_reward
            [QuestCompletionItem(World.item_by_id(World.ITEM_ID_GOBLIN_EAR), 1)]  # quest_completed_items
        )

        retrieveDragonScale = Quest(
            World.QUEST_ID_RETRIEVE_DRAGON_SCALE,
            "Retrieve a Dragon Scale",
            "Venture into the Dragon's Lair and bring back a dragon scale. You will receive a magic potion and 100 gold pieces.",
            200,
            100,
            World.item_by_id(World.ITEM_ID_MAGIC_POTION),  # item_reward
            [QuestCompletionItem(World.item_by_id(World.ITEM_ID_DRAGON_SCALE), 1)]  # quest_completed_items
        )

        World.Quests.append(clearAlchemistGarden)
        World.Quests.append(clearFarmersField)
        World.Quests.append(slayGoblinLeader)
        World.Quests.append(retrieveDragonScale)

    @staticmethod
    def populate_locations():
        home = Location(
            World.LOCATION_ID_HOME, 
            "Home", 
            "Your house. You really need to clean up the place.",
            None,  # item_required_to_enter
            None,  # quest_available_here
            None   # monster
        )

        townSquare = Location(
            World.LOCATION_ID_TOWN_SQUARE, 
            "Town square", 
            "You see a fountain.",
            None,
            None,
            None
        )

        alchemistHut = Location(
            World.LOCATION_ID_ALCHEMIST_HUT, 
            "Alchemist's hut", 
            "There are many strange plants on the shelves.",
            None,  # item_required_to_enter
            World.quest_by_id(World.QUEST_ID_CLEAR_ALCHEMIST_GARDEN),  # quest_available_here
            None   # monster
        )

        alchemistsGarden = Location(
            World.LOCATION_ID_ALCHEMISTS_GARDEN, 
            "Alchemist's garden", 
            "Many plants are growing here.",
            None,
            None,
            World.monster_by_id(World.MONSTER_ID_RAT)
        )

        farmhouse = Location(
            World.LOCATION_ID_FARMHOUSE, 
            "Farmhouse", 
            "There is a small farmhouse, with a farmer in front.",
            None,
            World.quest_by_id(World.QUEST_ID_CLEAR_FARMERS_FIELD),
            None
        )

        farmersField = Location(
            World.LOCATION_ID_FARM_FIELD, 
            "Farmer's field", 
            "You see rows of vegetables growing here.",
            None,  # item_required_to_enter
            None,  # quest_available_here
            World.monster_by_id(World.MONSTER_ID_SNAKE)  # monster
        )

        guardPost = Location(
            World.LOCATION_ID_GUARD_POST, 
            "Guard post", 
            "There is a large, tough-looking guard here.", 
            World.item_by_id(World.ITEM_ID_ADVENTURER_PASS),
            None,
            None
        )

        bridge = Location(
            World.LOCATION_ID_BRIDGE, 
            "Bridge", 
            "A stone bridge crosses a wide river.",
            None,
            None,
            None
        )

        spiderField = Location(
            World.LOCATION_ID_SPIDER_FIELD, 
            "Forest", 
            "You see spider webs covering covering the trees in this forest.",
            None,
            None,
            World.monster_by_id(World.MONSTER_ID_GIANT_SPIDER)
        )

        darkForest = Location(
            World.LOCATION_ID_DARK_FOREST, 
            "Dark Forest", 
            "The trees are thick and the light is dim. Goblins are known to lurk here.",
            None,
            World.quest_by_id(World.QUEST_ID_SLAY_GOBLIN_LEADER),
            World.monster_by_id(World.MONSTER_ID_GOBLIN)
        )

        goblinCave = Location(
            World.LOCATION_ID_GOBLIN_CAVE, 
            "Goblin Cave", 
            "A dark, damp cave. You hear the growls of goblins.",
            None,
            None,
            World.monster_by_id(World.MONSTER_ID_GOBLIN)
        )

        dragonLair = Location(
            World.LOCATION_ID_DRAGON_LAIR, 
            "Dragon's Lair", 
            "A massive cavern with the bones of many adventurers. A dragon resides here.",
            None,
            World.quest_by_id(World.QUEST_ID_RETRIEVE_DRAGON_SCALE),
            World.monster_by_id(World.MONSTER_ID_DRAGON)
        )

        magicShop = Location(
            World.LOCATION_ID_MAGIC_SHOP, 
            "Magic Shop", 
            "A small shop filled with potions and magical artifacts.",
            None,
            None,
            None
        )

        home.location_to_north = townSquare

        townSquare.location_to_north = alchemistHut
        townSquare.location_to_south = home
        townSquare.location_to_east = guardPost
        townSquare.location_to_west = farmhouse

        farmhouse.location_to_east = townSquare
        farmhouse.location_to_west = farmersField

        farmersField.location_to_east = farmhouse

        alchemistHut.location_to_south = townSquare
        alchemistHut.location_to_north = alchemistsGarden

        alchemistsGarden.location_to_south = alchemistHut

        guardPost.location_to_east = bridge
        guardPost.location_to_west = townSquare

        bridge.location_to_west = guardPost
        bridge.location_to_east = spiderField

        spiderField.location_to_west = bridge
        spiderField.location_to_north = darkForest

        darkForest.location_to_south = spiderField
        darkForest.location_to_north = goblinCave

        goblinCave.location_to_south = darkForest

        magicShop.location_to_west = townSquare
        magicShop.location_to_east = dragonLair

        dragonLair.location_to_west = magicShop

        World.Locations.append(home)
        World.Locations.append(townSquare)
        World.Locations.append(guardPost)
        World.Locations.append(alchemistHut)
        World.Locations.append(alchemistsGarden)
        World.Locations.append(farmhouse)
        World.Locations.append(farmersField)
        World.Locations.append(bridge)
        World.Locations.append(spiderField)
        World.Locations.append(darkForest)
        World.Locations.append(goblinCave)
        World.Locations.append(dragonLair)
        World.Locations.append(magicShop)

    @staticmethod
    def item_by_id(id):
        for item in World.Items:
            if item.id == id:
                return item
        return None

    @staticmethod
    def monster_by_id(id):
        for monster in World.Monsters:
            if monster.id == id:
                return monster
        return None

    @staticmethod
    def quest_by_id(id):
        for quest in World.Quests:
            if quest.id == id:
                return quest
        return None

    @staticmethod
    def location_by_id(id):
        for location in World.Locations:
            if location.id == id:
                return location
        return None