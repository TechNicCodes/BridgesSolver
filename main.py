"""
File: main.py
Author: Nicholas Boylan
Date: 6-3-2024
Description: Runs the application. Creates the grid, asks for the input, then calls the solver to solve the puzzle
"""

from grid import Grid
from node import Node

def main():

    test_file_path = "TestPuzzles/Test1.txt" # CHOOSE TEST CASE HERE

    # Read in the test grid and convert it to a grid of nodes and a list of nodes
    my_grid = Grid(test_file_path)
    node_grid, node_list = Grid.grid_with_nodes(my_grid)

    # Uncomment to print all nodes and empty spaces in the grid
#    for row in node_grid:
#        for node in row:
#            print(node)
    # Uncomment to just print a list of nodes
#    for item in node_list:
#        print(item)


    #TODO: Run solving logic on the grid

if __name__ == "__main__":
    main()