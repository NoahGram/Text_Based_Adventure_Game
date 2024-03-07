from tkinter import Tk, Label, Button
from game_ui import GameUI

# Define the button
button1 = Button()

# Define the label
label1 = Label()

# Function to be called when the button is clicked
def button_click():
    label1.config(text="Button clicked!")

# Bind the button click event to the function
button1.config(command=button_click)