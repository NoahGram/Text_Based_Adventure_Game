# game_ui.py
import tkinter as tk
from tkinter import scrolledtext

class GameUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text-Based RPG Game")
        self.root.geometry("850x550")

        self.health = tk.StringVar()
        self.gold = tk.StringVar()
        self.lvl = tk.StringVar()
        
        # Starting values
        self.health.set(f"Health: {100}")
        self.gold.set(f"Gold: {0}")
        self.lvl.set(f"Lvl: {1}")

        # Top left Text Labels 
        self.health_label = tk.Label(self.root, textvariable=self.health, font=("Arial", 10))
        self.health_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        self.gold_label = tk.Label(self.root, textvariable=self.gold, font=("Arial", 10))
        self.gold_label.grid(row=0, column=0, padx=10, pady=35, sticky="nw")
        self.lvl_label = tk.Label(self.root, textvariable=self.lvl, font=("Arial", 10))
        self.lvl_label.grid(row=0, column=0, padx=10, pady=60, sticky="nw")

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

        # Bottom right control buttons
        self.control_frame = tk.Frame(self.root)
        self.control_frame.grid(row=1, column=2, padx=10, pady=10, sticky="se")

        self.up_button = tk.Button(self.control_frame, text="Up", width=10)
        self.up_button.grid(row=0, column=1, padx=5, pady=5)

        self.down_button = tk.Button(self.control_frame, text="Down", width=10)
        self.down_button.grid(row=2, column=1, padx=5, pady=5)

        self.left_button = tk.Button(self.control_frame, text="Left", width=10)
        self.left_button.grid(row=1, column=0, padx=5, pady=5)

        self.right_button = tk.Button(self.control_frame, text="Right", width=10)
        self.right_button.grid(row=1, column=2, padx=5, pady=5)

    def start(self):
        self.root.mainloop()