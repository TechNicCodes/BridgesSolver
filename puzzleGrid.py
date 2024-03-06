"""
File: puzzleGrid.py
Author: Nicholas Boylan
Date: 6-3-2024
Description: Creates the grid on which the puzzle lives
"""

def createGrid(gridHeight, gridWidth):

    gameGrid = [[] for _ in range(gridWidth)] * gridHeight

    return gameGrid