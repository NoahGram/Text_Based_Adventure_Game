
import tkinter as tk
from inventory_item import InventoryItem
from monster import Monster
from player import Player
from player_quest import PlayerQuest
from potion import Potion
from weapon import Weapon
from world import World


class SuperAdventure:
    def __init__(self):
        self._player = Player(10, 10, 20, 0, 1)
        self.move_to(World.location_by_id(World.LOCATION_ID_HOME))
        self._player.inventory.append(InventoryItem(World.item_by_id(World.ITEM_ID_RUSTY_SWORD), 1))

        self.lbl_hit_points = self._player.current_hit_points
        self.lbl_gold = self._player.gold
        self.lbl_experience = self._player.experience_points
        self.lbl_level = self._player.level

    def btn_north_click(self):
        self.move_to(self._player.current_location.location_to_north)

    def btn_east_click(self):
        self.move_to(self._player.current_location.location_to_east)

    def btn_south_click(self):
        self.move_to(self._player.current_location.location_to_south)

    def btn_west_click(self):
        self.move_to(self._player.current_location.location_to_west)

    def move_to(self, new_location):
        # Does the location have any required items
        if new_location.item_required_to_enter is not None:
            # See if the player has the required item in their inventory
            player_has_required_item = any(ii.details.id == new_location.item_required_to_enter.id for ii in self._player.inventory)

            if not player_has_required_item:
                # We didn't find the required item in their inventory, so display a message and stop trying to move
                self.rtb_messages += f"You must have a {new_location.item_required_to_enter.name} to enter this location.\n"
                return

        # Update the player's current location
        self._player.current_location = new_location

        # Show/hide available movement buttons
        self.btn_north.visible = (new_location.location_to_north is not None)
        self.btn_east.visible = (new_location.location_to_east is not None)
        self.btn_south.visible = (new_location.location_to_south is not None)
        self.btn_west.visible = (new_location.location_to_west is not None)

        # Display current location name and description
        self.rtb_location = f"{new_location.name}\n{new_location.description}\n"

        # Completely heal the player
        self._player.current_hit_points = self._player.maximum_hit_points

        # Update Hit Points in UI
        self.lbl_hit_points = self._player.current_hit_points

        # Does the location have a quest?
        if new_location.quest_available_here is not None:
            # See if the player already has the quest, and if they've completed it
            player_already_has_quest = False
            player_already_completed_quest = False

            for player_quest in self._player.quests:
                if player_quest.details.id == new_location.quest_available_here.id:
                    player_already_has_quest = True

                    if player_quest.is_completed:
                        player_already_completed_quest = True

            # See if the player already has the quest
            if player_already_has_quest:
                # If the player has not completed the quest yet
                if not player_already_completed_quest:
                    # See if the player has all the items needed to complete the quest
                    player_has_all_items_to_complete_quest = True

                    for qci in new_location.quest_available_here.quest_completion_items:
                        found_item_in_players_inventory = False

                        # Check each item in the player's inventory, to see if they have it, and enough of it
                        for ii in self._player.inventory:
                            # The player has this item in their inventory
                            if ii.details.id == qci.details.id:
                                found_item_in_players_inventory = True

                                if ii.quantity < qci.quantity:
                                    # The player does not have enough of this item to complete the quest
                                    player_has_all_items_to_complete_quest = False

                                    # There is no reason to continue checking for the other quest completion items
                                    break

                                # We found the item, so don't check the rest of the player's inventory
                                break

                        # If we didn't find the required item, set our variable and stop looking for other items
                        if not found_item_in_players_inventory:
                            # The player does not have this item in their inventory
                            player_has_all_items_to_complete_quest = False

                            # There is no reason to continue checking for the other quest completion items
                            break

                    # The player has all items required to complete the quest
                    if player_has_all_items_to_complete_quest:
                        # Display message
                        self.rtb_messages += f"\nYou complete the '{new_location.quest_available_here.name}' quest.\n"

                        # Remove quest items from inventory
                        for qci in new_location.quest_available_here.quest_completion_items:
                            for ii in self._player.inventory:
                                if ii.details.id == qci.details.id:
                                    # Subtract the quantity from the player's inventory that was needed to complete the quest
                                    ii.quantity -= qci.quantity
                                    break

                        # Give quest rewards
                        self.rtb_messages += f"You receive:\n{new_location.quest_available_here.reward_experience_points} experience points\n{new_location.quest_available_here.reward_gold} gold\n{new_location.quest_available_here.reward_item.name}\n\n"

                        self._player.experience_points += new_location.quest_available_here.reward_experience_points
                        self._player.gold += new_location.quest_available_here.reward_gold

                        # Add the reward item to the player's inventory
                        added_item_to_player_inventory = False

                        for ii in self._player.inventory:
                            if ii.details.id == new_location.quest_available_here.reward_item.id:
                                # They have the item in their inventory, so increase the quantity by one
                                ii.quantity += 1

                                added_item_to_player_inventory = True

                                break

                            # They didn't have the item, so add it to their inventory, with a quantity of 1
                            if not added_item_to_player_inventory:
                                self._player.inventory.append(InventoryItem(new_location.quest_available_here.reward_item, 1))

                            # Mark the quest as completed
                            # Find the quest in the player's quest list
                            for pq in self._player.quests:
                                if pq.details.id == new_location.quest_available_here.id:
                                    # Mark it as completed
                                    pq.is_completed = True
                                    break

                            # The player does not already have the quest
                            # Display the messages
                            self.rtb_messages += f"You receive the {new_location.quest_available_here.name} quest.\n"
                            self.rtb_messages += f"{new_location.quest_available_here.description}\n"
                            self.rtb_messages += "To complete it, return with:\n"
                            for qci in new_location.quest_available_here.quest_completion_items:
                                self.rtb_messages += f"{qci.quantity} {qci.details.name if qci.quantity == 1 else qci.details.name_plural}\n"
                            self.rtb_messages += "\n"

                            # Add the quest to the player's quest list
                            self._player.quests.append(PlayerQuest(new_location.quest_available_here))

                            # Does the location have a monster?
                            if new_location.monster_living_here is not None:
                                self.rtb_messages += f"You see a {new_location.monster_living_here.name}\n"

                                # Make a new monster, using the values from the standard monster in the World.Monster list
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
                            self.dgv_inventory.rows = []

                            for inventory_item in self._player.inventory:
                                if inventory_item.quantity > 0:
                                    self.dgv_inventory.rows.append([inventory_item.details.name, inventory_item.quantity])

                            # Refresh player's quest list
                            self.dgv_quests.rows = []

                            for player_quest in self._player.quests:
                                self.dgv_quests.rows.append([player_quest.details.name, player_quest.is_completed])

                            # Refresh player's weapons combobox
                            weapons = [inventory_item.details for inventory_item in self._player.inventory if isinstance(inventory_item.details, Weapon) and inventory_item.quantity > 0]

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
                            healing_potions = [inventory_item.details for inventory_item in self._player.inventory if isinstance(inventory_item.details, Potion) and inventory_item.quantity > 0]

                            if len(healing_potions) == 0:
                                # The player doesn't have any potions, so hide the potion combobox and "Use" button
                                self.cbo_potions.visible = False
                                self.btn_use_potion.visible = False
                            else:
                                self.cbo_potions.data_source = healing_potions
                                self.cbo_potions.display_member = "Name"
                                self.cbo_potions.value_member = "ID"

                                self.cbo_potions.selected_index = 0

                            def btn_use_weapon_click(self, event):
                                pass

                            def btn_use_potion_click(self, event):
                                pass