"""
File: main.py
Author: Nicholas Boylan
Date: 6-3-2024
Description: Runs the application. Creates the grid, asks for the input, then calls the solver to solve the puzzle
"""

from grid import Grid

def main():

    test_file_path = "TestPuzzles/Test1.txt" # CHOOSE TEST CASE HERE

    # Read in the test grid
    my_grid = Grid(test_file_path)
    print(my_grid.grid)

    #TODO: Convert my_grid into a grid of nodes. Create each node. Will need to create each node before I am able 
    # to calculate each nodes adjacent nodes. 
    for row in my_grid.grid:
        for space in row:
            print(space)

    #TODO: Run solving logic on the grid

if __name__ == "__main__":
    main()