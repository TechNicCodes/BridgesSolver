# Bridges Solver Plan

First, create the algorithm to solve a puzzle. For this step, I will use test case puzzles. These test cases are in the form of a text file, and will be read into the program using a function.

Once the logic is working, I will work on creating a GUI and input system for the user to input their own puzzle

## Implementation of the GUI

## Implementation of the Node System

## Solving Algorithm
 

## Calculating Bridges Logic ##

We will iterate through the nodes, calculating the SOLVED nodes and PARTIALLY SOLVED nodes.

**SOLVED NODE**
A node is SOLVED if:
    - it's availableBridges == (sum of all adjacent nodes' available bridges)
        In this case, we just make the necessary connections between the current node and it's adjacent nodes

**PARTIALLY SOLVED NODE**
A node is PARTIALLY SOLVED if:
    - it's availableBridges == (sum of all adjacent nodes' available bridges) - 1
        In this case, we can connect the current node to all adjacent nodes with 1 bridge, and update the nodes current and possible bridges

**1-1 RULE**
If two nodes with value 1 (or available bridges 1) are adjacent, they cannot be connected (unless the last remaining bridge in the puzzle)
If two (1) nodes connect, then they will not be able to connect back into the rest of the graph

**2-2 RULE**
If two nodes with value 2 are adjacent, they cannot be connect with both of their bridges
If two (2) nodes connect with both this bridges, they will not have any remaining bridges to connect to the rest of the graph
This is just an extension of the *1-1 Rule*. If two 2-2 Nodes are connected with one bridge, then they become 1 nodes each, meaning they can't be connected

I believe by iterating through the nodes, calculating the SOLVED and PARTIALLY SOLVED nodes, and repeating the process, the puzzle will solve.

