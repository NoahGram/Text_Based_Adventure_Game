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

        # Middle right Treeview for inventory
        self.inventory_treeview = ttk.Treeview(self.root, columns=('Name', 'Quantity'), show='headings')

        # Set the column names and widths
        self.inventory_treeview.heading('Name', text='Name')
        self.inventory_treeview.column('Name', width=197)
        self.inventory_treeview.heading('Quantity', text='Quantity')
        self.inventory_treeview.column('Quantity', width=100)

        # Place the Treeview widget on the grid
        self.inventory_treeview.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Lower right Treeview for quests
        self.quests_treeview = ttk.Treeview(self.root, columns=('Name', 'Done?'), show='headings')

        # Set the column names and widths
        self.quests_treeview.heading('Name', text='Name')
        self.quests_treeview.column('Name', width=197)
        self.quests_treeview.heading('Done?', text='Done?')
        self.quests_treeview.column('Done?', width=100)

        # Place the Treeview widget on the grid
        self.quests_treeview.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

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

        self.use_attack = tk.Button(self.dropdown_frame, text="Use", width=10, command=self.super_adventure.btn_use_weapon_click)
        self.use_attack.grid(row=1, column=0, padx=5, pady=5)

        self.action_attack = ttk.Combobox(self.dropdown_frame)
        self.action_attack.grid(row=1, column=1, padx=5, pady=5)

        self.use_potion = tk.Button(self.dropdown_frame, text="Use", width=10, command=self.super_adventure.btnUsePotion_Click)
        self.use_potion.grid(row=3, column=0, padx=5, pady=5)

        self.action_potion = ttk.Combobox(self.dropdown_frame)
        self.action_potion.grid(row=3, column=1, padx=5, pady=5)
        

        # Not needed i think :D
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
        self.experience.set(f"Exp: {self._player.experience_points}")
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
    
    

    def update_ui(self):
        # Update the player's stats
        self._player_stats_text.set(f"HP: {self._player.hp} XP: {self._player.xp} Level: {self._player.level}")

        # Update the player's inventory
        self.inventory_list.delete(0, tk.END)
        for item in self._player.inventory:
            self.inventory_list.insert(tk.END, item)

        # Update the player's location
        self.location_text.set(self._player.current_location)

    def start(self):
        self.root.mainloop()