"""
File: grid.py
Author: Nicholas Boylan
Date: 6-3-2024
Description: Creates the grid from the test text file, and returns a 2d array representing the grid
"""

from node import Node
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

    def grid_with_nodes(grid):

        # Create a new grid to hold the node grid in
        node_grid = []
        node_list = []

        rowsInd = 0
        
        for row in grid.grid:
            colsInd = 0
            grid_row = []
            for num in row:
                # For each space in the grid, if it is numeric, create a node. If not, skip it    
                if num != '-':
                    node = Node.create_node(num, (rowsInd, colsInd))
                    node_list.append(node)
                    grid_row.append(node)
                else:
                    grid_row.append('-') 
                colsInd += 1
            rowsInd += 1
            node_grid.append(grid_row)
        return node_grid, node_list
        
