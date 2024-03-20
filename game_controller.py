from game_ui import GameUI

class GameController:
    def __init__(self):
        self.ui = GameUI()

        # Bind the button click event to the function
        self.ui.button1.config(command=lambda: self.button1_click())
        self.ui.button2.config(command=lambda: self.button2_click())
        self.ui.button3.config(command=lambda: self.button3_click())
        self.ui.button4.config(command=lambda: self.button4_click())

    def button1_click(self):
        current_text = self.ui.health.get()
        current_value = int(current_text.split(": ")[1])
        current_value += 1
        self.ui.health.set(f"Health: {current_value}")

    def button2_click(self):
        current_text = self.ui.gold.get()
        current_value = int(current_text.split(": ")[1])
        current_value += 1
        self.ui.gold.set(f"Gold: {current_value}")

    def button3_click(self):
        current_text = self.ui.lvl.get()
        current_value = int(current_text.split(": ")[1])
        current_value += 1
        self.ui.lvl.set(f"Lvl: {current_value}")

    def button4_click(self):
        self.ui.health.set(f"Health: {100}")
        self.ui.gold.set(f"Gold: {0}")
        self.ui.lvl.set(f"Lvl: {1}")

    def start(self):
        self.ui.start()
