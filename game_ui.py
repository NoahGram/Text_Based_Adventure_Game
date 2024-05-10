# game_ui.py
import tkinter as tk
from tkinter import scrolledtext, ttk
from player import Player
from weapon import Weapon

class GameUI:
    def __init__(self, super_adventure):

        self.root = tk.Tk()
        self.root.title("Text-Based RPG Game")
        self.root.geometry("850x550")

        # Player Instance
        self.super_adventure = super_adventure
        self._player = self.super_adventure._player

        self.health = tk.StringVar()
        self.gold = tk.StringVar()
        self.experience = tk.StringVar()
        self.lvl = tk.StringVar()
        
        # Starting values
        self.update_stats()

        # Top left Text Labels 
        self.health_label = tk.Label(self.root, textvariable=self.health, font=("Arial", 10))
        self.health_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        self.gold_label = tk.Label(self.root, textvariable=self.gold, font=("Arial", 10))
        self.gold_label.grid(row=0, column=0, padx=10, pady=35, sticky="nw")
        self.experience_label = tk.Label(self.root, textvariable=self.experience, font=("Arial", 10))
        self.experience_label.grid(row=0, column=0, padx=10, pady=60, sticky="nw")
        self.lvl_label = tk.Label(self.root, textvariable=self.lvl, font=("Arial", 10))
        self.lvl_label.grid(row=0, column=0, padx=10, pady=85, sticky="nw")

        # Top right rich-text box
        self.top_right_text = scrolledtext.ScrolledText(self.root, width=40, height=10, wrap=tk.WORD)
        self.top_right_text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Middle right rich-text box
        self.middle_right_text = scrolledtext.ScrolledText(self.root, width=40, height=20, wrap=tk.WORD)
        self.middle_right_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Lower right rich-text box for quests
        self.lower_right_text_quests = scrolledtext.ScrolledText(self.root, width=40, height=30, wrap=tk.WORD)
        self.lower_right_text_quests.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Bottom left 2x2 grid
        self.bottom_left_frame = tk.Frame(self.root)
        self.bottom_left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="sw")

        self.button1 = tk.Button(self.bottom_left_frame, text="Button 1", width=10)
        self.button1.grid(row=0, column=0, padx=5, pady=5)

        self.button2 = tk.Button(self.bottom_left_frame, text="Button 2", width=10)
        self.button2.grid(row=0, column=1, padx=5, pady=5)
        self.button3 = tk.Button(self.bottom_left_frame, text="Button 3", width=10)
        self.button3.grid(row=1, column=0, padx=5, pady=5)

        self.button4 = tk.Button(self.bottom_left_frame, text="Button 4", width=10)
        self.button4.grid(row=1, column=1, padx=5, pady=5)

        # Top right control buttons
        self.control_frame = tk.Frame(self.root)
        self.control_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ne")

        self.north_button = tk.Button(self.control_frame, text="North", width=10, command=self.super_adventure.btnNorth_Click)
        self.north_button.grid(row=0, column=1, padx=5, pady=5)

        self.south_button = tk.Button(self.control_frame, text="South", width=10, command=self.super_adventure.btnSouth_Click)
        self.south_button.grid(row=2, column=1, padx=5, pady=5)

        self.west_button = tk.Button(self.control_frame, text="West", width=10, command=self.super_adventure.btnWest_Click)
        self.west_button.grid(row=1, column=0, padx=5, pady=5)

        self.east_button = tk.Button(self.control_frame, text="East", width=10, command=self.super_adventure.btnEast_Click)
        self.east_button.grid(row=1, column=2, padx=5, pady=5)

        # Dropdowns
        self.dropdown_frame = tk.Frame(self.root)
        self.dropdown_frame.grid(row=1, column=2, padx=10, pady=10, sticky="ne")

        self.action_label = tk.Label(self.dropdown_frame, text="Select Action", font=("Arial", 10))
        self.action_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        self.use_attack = tk.Button(self.dropdown_frame, text="Use", width=10)
        self.use_attack.grid(row=1, column=0, padx=5, pady=5)

        self.action_attack = ttk.Combobox(self.dropdown_frame)
        self.action_attack.grid(row=1, column=1, padx=5, pady=5)

        self.use_potion = tk.Button(self.dropdown_frame, text="Use", width=10)
        self.use_potion.grid(row=3, column=0, padx=5, pady=5)

        self.action_potion = ttk.Combobox(self.dropdown_frame)
        self.action_potion.grid(row=3, column=1, padx=5, pady=5)

        # Create the weapons combobox
        self.cbo_weapons = ttk.Combobox(self.dropdown_frame)
        self.cbo_weapons.grid(column=0, row=0)

        # Get the player's weapons
        weapons = [item for item in self._player.inventory if isinstance(item, Weapon)]

        # Update the weapons combobox
        self.cbo_weapons['values'] = weapons
        # Connect the button click events to the movement methods in the SuperAdventure class
        self.north_button = tk.Button(self.control_frame, text="North", width=10, command=self.super_adventure.btnNorth_Click)
        self.north_button.grid(row=0, column=1, padx=5, pady=5)

        self.south_button = tk.Button(self.control_frame, text="South", width=10, command=self.super_adventure.btnSouth_Click)
        self.south_button.grid(row=2, column=1, padx=5, pady=5)

        self.west_button = tk.Button(self.control_frame, text="West", width=10, command=self.super_adventure.btnWest_Click)
        self.west_button.grid(row=1, column=0, padx=5, pady=5)

        self.east_button = tk.Button(self.control_frame, text="East", width=10, command=self.super_adventure.btnEast_Click)
        self.east_button.grid(row=1, column=2, padx=5, pady=5)

    def update_stats(self):
        self.health.set(f"Health: {self._player.current_hit_points}")
        self.gold.set(f"Gold: {self._player.gold}")
        self.experience.set(f"Exp: {self._player.experiencePoints}")
        self.lvl.set(f"Lvl: {self._player.level}")

    def update_buttons(self, new_location):
        if new_location.location_to_north is not None:
            self.north_button.config(state='normal')
        else:
            self.north_button.config(state='disabled')

        if new_location.location_to_south is not None:
            self.south_button.config(state='normal')
        else:
            self.south_button.config(state='disabled')

        if new_location.location_to_west is not None:
            self.west_button.config(state='normal')
        else:
            self.west_button.config(state='disabled')

        if new_location.location_to_east is not None:
            self.east_button.config(state='normal')
        else:
            self.east_button.config(state='disabled')
    
    

    def use_weapon(self):
        # Get the currently selected weapon from the action_attack Combobox
        current_weapon = self.action_attack.get()

        # Calculate the amount of damage to do to the monster
        damage_to_monster = random.randint(current_weapon.minimum_damage, current_weapon.maximum_damage)

        # Apply the damage to the monster's current hit points
        self._current_monster.current_hit_points -= damage_to_monster

        # Display message
        self.top_right_text.insert(tk.END, f"You hit the {self._current_monster.name} for {damage_to_monster} points.\n")

        # Check if the monster is dead
        if self._current_monster.current_hit_points <= 0:
            # Monster is dead
            self.top_right_text.insert(tk.END, f"You defeated the {self._current_monster.name}.\n")

            # TODO: Give player experience points for killing the monster

    def use_potion(self):
        # Get the currently selected potion from the action_potion Combobox
        potion = self.action_potion.get()

        # Increase player's current hit points, but not beyond their maximum hit points
        self._player.current_hit_points = min(self._player.current_hit_points + potion.amount_to_heal, self._player.maximum_hit_points)

        # Remove the potion from the player's inventory
        self._player.inventory.remove(potion)

        # Display message
        self.top_right_text.insert(tk.END, f"You drink a {potion.name}.\n")

    def update_ui(self):
        # Update the player's stats
        self._player_stats_text.set(f"HP: {self._player.hp} XP: {self._player.xp} Level: {self._player.level}")

        # Update the player's inventory
        self.inventory_list.delete(0, tk.END)
        for item in self._player.inventory:
            self.inventory_list.insert(tk.END, item)

        # Update the player's location
        self.location_text.set(self._player.location)

    def north_button_click(self):
        # Move the player to the north
        self._player.move_north()

    def east_button_click(self):
        # Move the player to the east
        self._player.move_east()

    def south_button_click(self):
        # Move the player to the south
        self._player.move_south()

    def west_button_click(self):
        # Move the player to the west
        self._player.move_west()

    def start(self):
        self.root.mainloop()