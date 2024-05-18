# SuperAdventure.py
import random
import tkinter as tk
from game_ui import GameUI
from monster import Monster
from player import Player
from potion import Potion
from weapon import Weapon
from world import World
from inventory_item import InventoryItem

class SuperAdventure:
    def __init__(self):
        World.__init__()
        self._player = Player(10, 10, 20, 0, 1)
        self.game_ui = GameUI(self)
        self.move_to(World.location_by_id(World.LOCATION_ID_HOME))
        self._player.inventory.append(InventoryItem(World.item_by_id(World.ITEM_ID_RUSTY_SWORD), 1))
        self._player.inventory.append(InventoryItem(World.item_by_id(World.ITEM_ID_IRON_SWORD), 1))
        self._player.inventory.append(InventoryItem(World.item_by_id(World.ITEM_ID_HEALING_POTION), 4))
        self._player.inventory.append(InventoryItem(World.item_by_id(World.ITEM_ID_ADVENTURER_PASS), 1))

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

    def btn_use_weapon_click(self, sender, e):
        pass

    def btn_use_potion_click(self, sender, e):
        pass

    
    def move_to(self, new_location):
        # Does the location have any required items
        if new_location.item_required_to_enter != None:
            #player_has_required_item = any(ii.details.id == new_location.item_required_to_enter.id for ii in self._player.inventory)
            # See if the player has the required item in their inventory
            player_has_required_item = False

            for ii in self._player.inventory:
                if ii.details.id == new_location.item_required_to_enter.id:
                    # We found the required item
                    player_has_required_item = True
                    break

            if not player_has_required_item:
                # We didn't find the required item in their inventory, so display a message and stop trying to move
                self.game_ui.top_right_text.insert('end', f"You receive:\n{new_location.quest_available_here.experience_points_reward} experience points\n{new_location.quest_available_here.gold_reward} gold\n{new_location.quest_available_here.item_reward.name}\n\n")
                return

        # Update the player's current location
        self._player.current_location = new_location

        # Show/hide available movement buttons
        #self.btn_north.visible = (new_location.location_to_north is not None)
        #self.btn_east.visible = (new_location.location_to_east is not None)
        #self.btn_south.visible = (new_location.location_to_south is not None)
        #self.btn_west.visible = (new_location.location_to_west is not None)

        # Display current location name and description
        location_text = f"{new_location.name}\n{new_location.description}\n"
        self.game_ui.top_right_text.insert(tk.INSERT, location_text)
        self.game_ui.top_right_text.see(tk.END)

        # Completely heal the player
        self._player.current_hit_points = self._player.maximum_hit_points

        # Update Hit Points in UI
        self.game_ui.update_stats()

        # Does the location have a quest?
        if new_location.quest_available_here is not None:
            # See if the player already has the quest, and if they've completed it
            player_already_has_quest = False
            player_already_completed_quest = False

            for player_quest in self._player.quests:
                if player_quest.id == new_location.quest_available_here.id:
                    player_already_has_quest = True

                    if player_quest.quest_completion:
                        player_already_completed_quest = True

            # See if the player already has the quest
            if player_already_has_quest:
                # If the player has not completed the quest yet
                if not player_already_completed_quest:
                    # See if the player has all the items needed to complete the quest
                    player_has_all_items_to_complete_quest = True
                    #!!!!!!!!!!!!!!!!!!!!!
                    for qci in new_location.quest_available_here.quest_completion_items:
                        found_item_in_players_inventory = False

                        # Check each item in the player's inventory, to see if they have it, and enough of it
                        for ii in self._player.inventory:
                            # The player has this item in their inventory
                            #!!!!!!!!!!!!!!!!!!!
                            if ii.details.id == qci.details.id:
                                found_item_in_players_inventory = True
                                #!!!!!!!!!!!!!!!!!!!
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
                        # Display quest completion message
                        quest_completion_message = f"\nYou complete the '{new_location.quest_available_here.name}' quest.\n"
                        self.game_ui.top_right_text.insert(tk.INSERT, quest_completion_message)
                        self.game_ui.top_right_text.see(tk.END)

                        # Display current location name and description
                        location_text = f"{new_location.name}\n{new_location.description}\n"
                        self.game_ui.top_right_text.insert(tk.INSERT, location_text)
                        self.game_ui.top_right_text.see(tk.END)

                        # Remove quest items from inventory
                        for qci in new_location.quest_available_here.quest_completion_items:
                            for ii in self._player.inventory:
                                if ii.details.id == qci.details.id:
                                    # Subtract the quantity from the player's inventory that was needed to complete the quest
                                    ii.quantity -= qci.quantity
                                    break

                        # Give quest rewards
                        self.game_ui.top_right_text.insert('end', f"You receive:\n{new_location.quest_available_here.experience_points_reward} experience points\n{new_location.quest_available_here.gold_reward} gold\n{new_location.quest_available_here.item_reward.name}\n\n")

                        self._player.experience_points += new_location.quest_available_here.experience_points_reward
                        self._player.gold += new_location.quest_available_here.gold_reward

                        # Add the reward item to the player's inventory
                        added_item_to_player_inventory = False

                        for ii in self._player.inventory:
                            if ii.details.id == new_location.quest_available_here.item_reward.id:
                                # They have the item in their inventory, so increase the quantity by one
                                ii.quantity += 1

                                added_item_to_player_inventory = True

                                break

                            # They didn't have the item, so add it to their inventory, with a quantity of 1
                            if not added_item_to_player_inventory:
                                self._player.inventory.append(InventoryItem(new_location.quest_available_here.item_reward, 1))

                            # Mark the quest as completed
                            # Find the quest in the player's quest list
                            for pq in self._player.quests:
                                if pq.id == new_location.quest_available_here.id:  # Changed this line
                                    # Mark it as completed
                                    pq.is_completed = True
                                    break

            #Missing Else statement
            else:
                # The player does not already have the quest
                # Display quest the messages
                quest_message = f"You receive the {new_location.quest_available_here.name} quest.\n"
                quest_message += f"{new_location.quest_available_here.description}\n"
                quest_message += "To complete it, return with:\n"
                self.game_ui.top_right_text.insert(tk.INSERT, quest_message)
                self.game_ui.top_right_text.see(tk.END)

                for qci in new_location.quest_available_here.quest_completion_items:
                    quest_completion_item_message = f"{qci.quantity} {qci.details.name if qci.quantity == 1 else qci.details.name_plural}\n"
                    self.game_ui.top_right_text.insert(tk.INSERT, quest_completion_item_message)
                self.game_ui.top_right_text.insert(tk.INSERT, "\n")
                self.game_ui.top_right_text.see(tk.END)

                # Add the quest to the player's quest list
                self._player.quests.append(new_location.quest_available_here)

        # Does the location have a monster?
        if new_location.monster_living_here is not None:
            monster_message = f"You see a {new_location.monster_living_here.name}\n"
            self.game_ui.top_right_text.insert(tk.INSERT, monster_message)
            self.game_ui.top_right_text.see(tk.END)

            # Make a new monster, using the values from the standard monster in the World.Monster list
            standard_monster = World.monster_by_id(new_location.monster_living_here.id)

            self._current_monster = Monster(standard_monster.id, standard_monster.name, standard_monster.maximum_damage,
                                            standard_monster.experience_points_reward, standard_monster.gold_reward, standard_monster.current_hit_points, standard_monster.maximum_hit_points)

            for loot_item in standard_monster.loot_table:
                self._current_monster.loot_table.append(loot_item)

            # Make the dropdowns and buttons visible
            self.game_ui.action_attack.grid()
            self.game_ui.use_attack.grid()
            self.game_ui.action_potion.grid()
            self.game_ui.use_potion.grid()
        else:
            self._current_monster = None

            # Make the dropdowns and buttons invisible
            self.game_ui.action_attack.grid_remove()
            self.game_ui.use_attack.grid_remove()
            self.game_ui.action_potion.grid_remove()
            self.game_ui.use_potion.grid_remove()

        # Refresh player's inventory list
        self.game_ui.inventory_treeview.delete(*self.game_ui.inventory_treeview.get_children())

        # Populate the Treeview with the player's inventory
        for inventory_item in self._player.inventory:
            if inventory_item.quantity > 0:
                self.game_ui.inventory_treeview.insert('', 'end', values=(inventory_item.details.name, inventory_item.quantity))

        # Refresh player's quest list
        self.game_ui.quests_treeview.delete(*self.game_ui.quests_treeview.get_children())

       # Populate the Treeview with the player's quests
        for player_quest in self._player.quests:
            quest_status = "Yes" if player_quest.is_completed else "No"
            self.game_ui.quests_treeview.insert('', 'end', values=(player_quest.name, quest_status))

        # Refresh player's weapons combobox
        weapons = [inventory_item.details for inventory_item in self._player.inventory if isinstance(inventory_item.details, Weapon) and inventory_item.quantity > 0]

        if len(weapons) == 0:
            # The player doesn't have any weapons, so hide the weapon combobox and "Use" button
            self.game_ui.action_attack.state(['active'])
            self.game_ui.use_attack.config(state='active')
        else:
            # Clear the Combobox
            self.game_ui.action_attack.set('')
            self.game_ui.action_attack['values'] = [weapon.name for weapon in weapons]

            # Select the first weapon in the list
            self.game_ui.action_attack.current(0)

            # Enable the Combobox and "Use" button
            self.game_ui.action_attack.state(['active'])
            self.game_ui.use_attack.config(state='active')

        # Refresh player's potions combobox
        potions = [inventory_item.details for inventory_item in self._player.inventory if isinstance(inventory_item.details, Potion) and inventory_item.quantity > 0]

        if len(potions) == 0:
            # The player doesn't have any potions, so hide the potion combobox and "Use" button
            self.game_ui.action_potion.state(['active'])
            self.game_ui.use_potion.config(state='active')
        else:
            # Clear the Combobox
            self.game_ui.action_potion.set('')
            self.game_ui.action_potion['values'] = [potion.name for potion in potions]

            # Select the first potion in the list
            self.game_ui.action_potion.current(0)

            # Enable the Combobox and "Use" button
            self.game_ui.action_potion.state(['active'])
            self.game_ui.use_potion.config(state='active')



    def btn_use_weapon_click(self):
        # Get the currently selected weapon name from the cboWeapons ComboBox
        current_weapon_name = self.game_ui.action_attack.get()

        # Find the weapon object that corresponds to the selected name
        current_weapon = next((item.details for item in self._player.inventory if isinstance(item.details, Weapon) and item.details.name == current_weapon_name), None)

        if current_weapon is not None:
            # Determine the amount of damage to do to the monster
            damage_to_monster = random.randint(current_weapon.minimum_damage, current_weapon.maximum_damage)
            # Apply the damage to the monster's current_hit_points
            self._current_monster.current_hit_points -= damage_to_monster
            # Display message
            self.game_ui.top_right_text.insert('end', f"You hit the {self._current_monster.name} for {damage_to_monster} points.\n")
                
        # Check if the monster is dead
        if self._current_monster.current_hit_points <= 0:
            # Monster is dead
            self.game_ui.top_right_text.insert('end', "\n")
            self.game_ui.top_right_text.insert('end', f"You defeated the {self._current_monster.name}\n")
            # Give player experience points for killing the monster
            self._player.experience_points += self._current_monster.experience_points_reward
            self.game_ui.top_right_text.insert('end', f"You receive {self._current_monster.experience_points_reward} experience points\n")
            # Give player gold for killing the monster 
            self._player.gold += self._current_monster.gold_reward
            self.game_ui.top_right_text.insert('end', f"You receive {self._current_monster.gold_reward} gold\n")
            # Get random loot items from the monster
            looted_items = []
            # Add items to the lootedItems list, comparing a random number to the drop percentage
            for loot_item in self._current_monster.loot_table:
                if random.randint(1, 100) <= loot_item.drop_rate:
                    looted_items.append(InventoryItem(loot_item.details, 1))
            # If no items were randomly selected, then add the default loot item(s).
            if len(looted_items) == 0:
                for loot_item in self._current_monster.loot_table:
                    if loot_item.is_default_item:
                        looted_items.append(InventoryItem(loot_item.details, 1))
            # Add the looted items to the player's inventory
            for inventory_item in looted_items:
                self._player.add_item_to_inventory(inventory_item)  # Changed this line
                if inventory_item.quantity == 1:
                    self.game_ui.top_right_text.insert('end', f"You loot {inventory_item.quantity} {inventory_item.details.name}\n")
                else:
                    self.game_ui.top_right_text.insert('end', f"You loot {inventory_item.quantity} {inventory_item.details.name_plural}\n")
            # Refresh player information and inventory controls
            self.game_ui.update_stats()
            #self.update_inventory_list_in_ui()
            #self.update_weapon_list_in_ui()
            #self.update_potion_list_in_ui()
            # Add a blank line to the messages box, just for appearance.
            self.game_ui.top_right_text.insert('end', "\n")
            # Move player to current location (to heal player and create a new monster to fight)
            self.move_to(self._player.current_location)
        else:
            # Monster is still alive
            # Determine the amount of damage the monster does to the player
            damage_to_player = random.randint(0, self._current_monster.maximum_damage)
            # Display message
            self.game_ui.top_right_text.insert('end', f"The {self._current_monster.name} did {damage_to_player} points of damage.\n")
            # Subtract damage from player
            self._player.current_hit_points -= damage_to_player
            # Refresh player data in UI
            self.game_ui.update_stats()
            if self._player.current_hit_points <= 0:
                # Display message
                self.game_ui.top_right_text.insert('end', f"The {self._current_monster.name} killed you.\n")
                # Move player to "Home"
                self.move_to(World.location_by_id(World.LOCATION_ID_HOME))


    def btnUsePotion_Click(self):
        # Get the currently selected potion from the combobox
        potion = self.game_ui.action_potion.get()  # Assuming cboPotions is a tkinter Combobox

        # Add healing amount to the player's current hit points
        self._player.current_hit_points += potion.amount_to_heal

        # CurrentHitPoints cannot exceed player's MaximumHitPoints
        if self._player.current_hit_points > self._player.maximum_hit_points:
            self._player.current_hit_points = self._player.maximum_hit_points

        # Remove the potion from the player's inventory
        for ii in self._player.inventory:
            if ii.Details.id == potion.id:
                ii.Quantity -= 1
                break

        # Display message
        self.top_right_text.insert('end', f"You drink a {potion.Name}\n")

        # Monster gets their turn to attack
        # Determine the amount of damage the monster does to the player
        damageToPlayer = random.randint(0, self._currentMonster.MaximumDamage)

        # Display message
        self.top_right_text.insert('end', f"The {self._currentMonster.Name} did {damageToPlayer} points of damage.\n")

        # Subtract damage from player
        self._player.CurrentHitPoints -= damageToPlayer

        if self._player.CurrentHitPoints <= 0:
            # Display message
            self.top_right_text.insert('end', f"The {self._currentMonster.Name} killed you.\n")

            # Move player to "Home"
            self.MoveTo(World.LocationByID(World.LOCATION_ID_HOME))  # Assuming MoveTo is a method in your class

        # Refresh player data in UI
        self.lblHitPoints['text'] = str(self._player.CurrentHitPoints)  # Assuming lblHitPoints is a tkinter Label

        #self.UpdateInventoryListInUI()  # Assuming UpdateInventoryListInUI is a method in your class
        #self.UpdatePotionListInUI()  # Assuming UpdatePotionListInUI is a method in your class


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