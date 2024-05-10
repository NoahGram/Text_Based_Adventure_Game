from game_ui import GameUI
from super_adventure import SuperAdventure

class GameController:
    def __init__(self):
        self.game = SuperAdventure()
        self.ui = GameUI(self.game)

        # Bind the button click event to the function
        self.ui.button1.config(command=lambda: self.button1_click())
        self.ui.button2.config(command=lambda: self.button2_click())
        self.ui.button3.config(command=lambda: self.button3_click())
        self.ui.button4.config(command=lambda: self.button4_click())

    def button1_click(self):
        self.game.increase_health()
        self.ui.update_ui()

    def button2_click(self):
        self.game.increase_gold()
        self.ui.update_ui()

    def button3_click(self):
        self.game.increase_level()
        self.ui.update_ui()

    def button4_click(self):
        self.game.reset()
        self.ui.update_ui()

    def north_button_click(self):
        # Move the player to the north
        self.game.btnNorth_Click()
        self.ui.update_ui()

    def east_button_click(self):
        # Move the player to the east
        self.game.btnEast_Click()
        self.ui.update_ui()

    def south_button_click(self):
        # Move the player to the south
        self.game.btnSouth_Click()
        self.ui.update_ui()

    def west_button_click(self):
        # Move the player to the west
        self.game.btnWest_Click()
        self.ui.update_ui()

    def start(self):
        self.ui.start()