"""
File: grid.py
Author: Nicholas Boylan
Date: 6-3-2024
Description: Creates the grid from the test text file, and returns a 2d array representing the grid
"""

class Grid:
    
    def __init__(self, test_file):
        self.grid = self.read_test_file(test_file)

    def read_test_file(self, test_file):
        grid = []
        with open(test_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    row = line.strip().strip('[],').split(',')
                    grid.append([int(x.strip()) if x.strip().isdigit() else x.strip() for x in row])
        return grid

        
        
