"""
File: node.py
Author: Nicholas Boylan
Date: 6-3-2024
Description: A new structure to hold all relevant information about a node in a bridges puzzle
"""

from dataclasses import dataclass

@dataclass
class Node:

    nodeValue: int    # number inside the node
    nodePosition: tuple    # coordinates in the grid. Also the identifying aspect of a node
    adjacentNodes: list = None   # a list of other nodes which the current node can see in the grid
    bridges: list = None   # a list of nodes that are connected to the current node
    availableBridges: int = None   # a derived number, kept for convienience. nodeValue - len(bridges)

    def create_node(value, position):

        node = Node()
        node.nodeValue = value
        node.nodePosition = position

    
    # Reduces the value of a node. Used when creating a bridge between nodes