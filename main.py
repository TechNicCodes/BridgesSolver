"""
File: main.py
Author: Nicholas Boylan
Date: 6-3-2024
Description: Runs the application. Creates the grid, asks for the input, then calls the solver to solve the puzzle
"""

from puzzleGrid import createGrid


# Create a few variables for the grid and set default values
gridHeight = 10
gridWidth = 10

# TODO: Ask the user to input the size of their puzzle

gameGrid = createGrid(gridHeight, gridWidth)

# TODO: Now present user with GUI with a text box in each square of the grid.
# A text box should default to 0, but the user can change it (only numbers 1-8)
# to input a node. The number they put in is the value of the node

# Once the grid is established, each input should create a node, and it should be 
# stored in the correspondind location in the grid




