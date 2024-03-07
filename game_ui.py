import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Text and Controls Layout")
root.geometry("850x550")

# Top left title
health_label = tk.Label(root, text="Health: 0", font=("Arial", 10))
health_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
gold_label = tk.Label(root, text="Gold: 0", font=("Arial", 10))
gold_label.grid(row=0, column=0, padx=10, pady=35, sticky="nw")
lvl_label = tk.Label(root, text="Lvl: 0", font=("Arial", 10))
lvl_label.grid(row=0, column=0, padx=10, pady=60, sticky="nw")

# Top right rich-text box
top_right_text = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
top_right_text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Middle right rich-text box
middle_right_text = scrolledtext.ScrolledText(root, width=40, height=20, wrap=tk.WORD)
middle_right_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Bottom left 2x2 grid
bottom_left_frame = tk.Frame(root)
bottom_left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="sw")

button1 = tk.Button(bottom_left_frame, text="Button 1", width=10)
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(bottom_left_frame, text="Button 2", width=10)
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(bottom_left_frame, text="Button 3", width=10)
button3.grid(row=1, column=0, padx=5, pady=5)

button4 = tk.Button(bottom_left_frame, text="Button 4", width=10)
button4.grid(row=1, column=1, padx=5, pady=5)

# Bottom right control buttons
control_frame = tk.Frame(root)
control_frame.grid(row=1, column=2, padx=10, pady=10, sticky="se")

up_button = tk.Button(control_frame, text="Up", width=10)
up_button.grid(row=0, column=1, padx=5, pady=5)

down_button = tk.Button(control_frame, text="Down", width=10)
down_button.grid(row=2, column=1, padx=5, pady=5)

left_button = tk.Button(control_frame, text="Left", width=10)
left_button.grid(row=1, column=0, padx=5, pady=5)

right_button = tk.Button(control_frame, text="Right", width=10)
right_button.grid(row=1, column=2, padx=5, pady=5)

def button1_click():
    health_label.config(text="Health: 100")


def button2_click():
    gold_label.config(text="Gold: 420")


def button3_click():
    lvl_label.config(text="Lvl: 99")


def button4_click():
    health_label.config(text="Health: 0")
    gold_label.config(text="Gold: 0")
    lvl_label.config(text="Lvl: 0")

# Bind the button click event to the function
button1.config(command=button1_click)
button2.config(command=button2_click)
button3.config(command=button3_click)
button4.config(command=button4_click)

root.mainloop()
