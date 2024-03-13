"""
File: main.py
Author: Nicholas Boylan
Date: 13-3-2024
Description: Used for the creation of the UI 
"""

from tkinter import *


# UI should display a grid for the user. In each cell of the grid, there
# should be a text input box, where the user can input the value of a node
# at the position

root = Tk()
b = 0
for r in range(6):
    for c in range(6):
        b+b+1
        Button(root, text=str(b), borderwidth=1 ).grid(row=r, column=c)
root.mainloop()
