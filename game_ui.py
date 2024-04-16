# game_ui.py
import tkinter as tk
from tkinter import scrolledtext, ttk
from player import Player

class GameUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text-Based RPG Game")
        self.root.geometry("850x550")

        # Player Instance
        _player = Player(100, 100, 20, 0, 1)

        self.health = tk.StringVar()
        self.gold = tk.StringVar()
        self.experience = tk.StringVar()
        self.lvl = tk.StringVar()
        
        # Starting values
        self.health.set(f"Health: {_player.current_hit_points}")
        self.gold.set(f"Gold: {_player.gold}")
        self.experience.set(f"Exp: {_player.experiencePoints}")
        self.lvl.set(f"Lvl: {_player.level}")

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

        self.north_button = tk.Button(self.control_frame, text="North", width=10)
        self.north_button.grid(row=0, column=1, padx=5, pady=5)

        self.south_button = tk.Button(self.control_frame, text="South", width=10)
        self.south_button.grid(row=2, column=1, padx=5, pady=5)

        self.west_button = tk.Button(self.control_frame, text="West", width=10)
        self.west_button.grid(row=1, column=0, padx=5, pady=5)

        self.east_button = tk.Button(self.control_frame, text="East", width=10)
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
    
    def start(self):
        self.root.mainloop()