import os
import tkinter as tk
from tkinter import ttk, messagebox, Label, PhotoImage
import pyperclip
import random
import logging
from tkinter.constants import END
from helpers import generate_config
import command_generator
import command_data
# command_generator.py
from IMEICommandGenerator import IMEICommandGenerator

# Get the path to the current script directory
script_dir = os.path.dirname(__file__)

# Create the main window
root = tk.Tk()

# Load the image using a relative path
logo_path = os.path.join(script_dir, "Granite_Logo.png")
logo = PhotoImage(file=logo_path)

# Resize the image
logo = logo.subsample(40)  # Reduce the size by half

# Create a label to display the logo
logo_label = Label(root, image=logo)
logo_label.grid(row=0, column=1, sticky="ne", padx=10, pady=10)  # Adjust the position as needed

# Create an instance of the IMEICommandGenerator class
app = IMEICommandGenerator(root)

# Run the Tkinter event loop
root.mainloop()
