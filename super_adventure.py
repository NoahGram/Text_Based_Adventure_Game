# SuperAdventure.py
from game_ui import GameUI
from monster import Monster
from player import Player
from potion import Potion
from weapon import Weapon
from world import World
from inventory_item import InventoryItem
from game_ui import GameUI

class SuperAdventure:
    def __init__(self):
        World.__init__()
        self._player = Player(10, 10, 20, 0, 1)
        self.game_ui = GameUI(self)
        self.move_to(World.location_by_id(World.LOCATION_ID_HOME))
        self._player.inventory.append(InventoryItem(World.item_by_id(World.ITEM_ID_RUSTY_SWORD), 1))

        self.lblHitPoints = self._player.current_hit_points
        self.lblGold = self._player.gold
        self.lblExperience = self._player.experience_points
        self.lblLevel = self._player.level

    def btnNorth_Click(self):
        self.move_to(self._player.current_location.location_to_north)

    def btnEast_Click(self):
        self.move_to(self._player.current_location.location_to_east)

    def btnSouth_Click(self):
        self.move_to(self._player.current_location.location_to_south)

    def btnWest_Click(self):
        self.move_to(self._player.current_location.location_to_west)

    def move_to(self, new_location):
        # Check if the player has the required items to enter the new location
        if new_location.item_required_to_enter is not None:
            if not self._player.has_required_item(new_location.item_required_to_enter):
                self.top_right_text.insert(tk.END, f"You must have {new_location.item_required_to_enter.name} to enter this location.\n")
                return

        # Update the player's current location
        self._player.current_location = new_location

        # Update the state of the buttons
        self.game_ui.update_buttons(new_location)  # Assuming game_ui is an instance of the GameUI class

        # Update the visibility of the buttons based on the new location
        self.btnNorth_Click['state'] = 'normal' if new_location.LocationToNorth is not None else 'disabled'
        self.btnSouth_Click['state'] = 'normal' if new_location.LocationToSouth is not None else 'disabled'
        self.btnWest_Click['state'] = 'normal' if new_location.LocationToWest is not None else 'disabled'
        self.btnEast_Click['state'] = 'normal' if new_location.LocationToEast is not None else 'disabled'

        self.rtbLocation = f"{new_location.name}\n{new_location.description}\n"

        self._player.current_hit_points = self._player.maximum_hit_points

        self.lblHitPoints = self._player.current_hit_points

        if new_location.quest_available_here is not None:
            # ... rest of the code ...
            if new_location.quest_available_here is not None:
                # See if the player already has the quest, and if they've completed it
                quest = new_location.quest_available_here
                player_quest = Player.quests.find(quest) if Player.quests else None

            # See if the player already has the quest
            if player_quest is None:
                # The player does not already have the quest
                Player.quests.append(quest)

                # Display message for the quest
                print(f"You receive the {quest.name} quest.")
                print(quest.description)

                # Display the items needed to complete the quest
                print(f"To complete it, return with: {quest.item_required_to_complete}")
            else:
                # The player has already taken the quest
                if not player_quest.is_completed:
                    # Check if the player has all the items needed to complete the quest
                    if Player.has_required_item(quest.item_required_to_complete):
                        # The player can complete the quest
                        Player.remove_item(quest.item_required_to_complete)

                        # Give quest rewards
                        print(f"You complete the {quest.name} quest.")
                        Player.experience_points += quest.reward_experience
                        Player.gold += quest.reward_gold
                        print(f"You receive {quest.reward_experience} experience points and {quest.reward_gold} gold.")
                        player_quest.is_completed = True
                    else:
                        print(f"You do not have the required item to complete the {quest.name} quest.")
                else:
                    print(f"You have already completed the {quest.name} quest.")

        if new_location.monster_living_here is not None:
            self.rtb_messages += f"You see a {new_location.monster_living_here.name}\n"

            standard_monster = World.monster_by_id(new_location.monster_living_here.id)

            self._current_monster = Monster(standard_monster.id, standard_monster.name, standard_monster.maximum_damage,
                                             standard_monster.reward_experience_points, standard_monster.reward_gold, standard_monster.current_hit_points, standard_monster.maximum_hit_points)

            for loot_item in standard_monster.loot_table:
                self._current_monster.loot_table.append(loot_item)

            self.cbo_weapons.visible = True
            self.cbo_potions.visible = True
            self.btn_use_weapon.visible = True
            self.btn_use_potion.visible = True
        else:
            self._current_monster = None

            self.cbo_weapons.visible = False
            self.cbo_potions.visible = False
            self.btn_use_weapon.visible = False
            self.btn_use_potion.visible = False

        # Refresh player's inventory list
        self.dgv_inventory.row_headers_visible = False

        self.dgv_inventory.column_count = 2
        self.dgv_inventory.columns[0].name = "Name"
        self.dgv_inventory.columns[0].width = 197
        self.dgv_inventory.columns[1].name = "Quantity"

        self.dgv_inventory.rows.clear()

        for inventory_item in self._player.inventory:
            if inventory_item.quantity > 0:
                self.dgv_inventory.rows.add([inventory_item.details.name, str(inventory_item.quantity)])

        # Refresh player's quest list
        self.dgv_quests.row_headers_visible = False

        self.dgv_quests.column_count = 2
        self.dgv_quests.columns[0].name = "Name"
        self.dgv_quests.columns[0].width = 197
        self.dgv_quests.columns[1].name = "Done?"

        self.dgv_quests.rows.clear()

        for player_quest in self._player.quests:
            self.dgv_quests.rows.add([player_quest.details.name, str(player_quest.is_completed)])

        # Refresh player's weapons combobox
        weapons = []

        for inventory_item in self._player.inventory:
            if isinstance(inventory_item.details, Weapon):
                if inventory_item.quantity > 0:
                    weapons.append(inventory_item.details)

        if len(weapons) == 0:
            # The player doesn't have any weapons, so hide the weapon combobox and "Use" button
            self.cbo_weapons.visible = False
            self.btn_use_weapon.visible = False
        else:
            self.cbo_weapons.data_source = weapons
            self.cbo_weapons.display_member = "Name"
            self.cbo_weapons.value_member = "ID"

            self.cbo_weapons.selected_index = 0

        # Refresh player's potions combobox
        healing_potions = []

        for inventory_item in self._player.inventory:
            if isinstance(inventory_item.details, Potion):
                if inventory_item.quantity > 0:
                    healing_potions.append(inventory_item.details)

        if len(healing_potions) == 0:
            # The player doesn't have any potions, so hide the potion combobox and "Use" button
            self.cbo_potions.visible = False
            self.btn_use_potion.visible = False
        else:
            self.cbo_potions.data_source = healing_potions
            self.cbo_potions.display_member = "Name"
            self.cbo_potions.value_member = "ID"

            self.cbo_potions.selected_index = 0

    def btn_use_weapon_click(self, sender, e):
        pass

    def btn_use_potion_click(self, sender, e):
        pass

    def increase_health(self):
        self._player.current_hit_points += 1
        # Add the indented block of code here

    def increase_gold(self):
        self._player.gold += 1
        # Add the indented block of code here

    def increase_level(self):
        self._player.level += 1

    def reset(self):
        self._player.current_hit_points = 100
        self._player.gold = 0
        self._player.level = 1