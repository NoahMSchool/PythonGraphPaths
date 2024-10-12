import pygame
from node import *

#########################################################
# Class for a generic graph
#########################################################
class Graph:
  def __init__(self):
    self.nodes = []
      

  ######################################################### 
  # Game Loop Functions
  #########################################################  
  def update(self, clock):
      pass
      
  def draw(self, screen):
    mapscale = 50
    for n in self.nodes:
      n.draw_node_connections(screen, mapscale)
    for n in self.nodes:
      n.draw_node(screen, mapscale)

  ######################################################### 
  # Node handling functions
  #########################################################  
  def return_nodes(self):
    return self.nodes

  def add_node(self, Node):
    self.nodes.append(Node)

  def remove_node(self, r):
    self.nodes.remove(r)
    # Once we have removed a node, we also remove all connections that
    # end with that node
    for n in self.nodes:
        for c in n.get_connections():
            if c.end == r:
                n.remove_connection(c)
  
  def has_node(self, node):
    for n in self.nodes:
      if n == node:
        return True
    return False

  def get_node(self, position):
    for n in self.nodes:
      if n.position.x == position.x and n.position.y == position.y:
        return n

  def get_node_connections(self, node):
    return node.get_connections()

#########################################################
# Helper functions to get example graphs
#########################################################

def get_grid_graph(gridsize):
    gridGraph = Graph()
    gridsize = 10
    
    for y in range(gridsize):
      for x in range(gridsize):
         gridGraph.add_node(Node(Position(x,y)))
    
    square = [(1,0),(0,1),(-1,0),(0,-1)]
    diagonals = [(1,1),(1,-1),(-1,1),(-1,-1)]
    directions = square + diagonals
    for n in gridGraph.return_nodes():
        for d in directions:
            target = gridGraph.get_node(Position(n.position.x + d[0], n.position.y + d[1]))
            if gridGraph.has_node(target):
                n.add_connections([Route(target, 1)])
    gridGraph.remove_node(gridGraph.get_node(Position(3,0)))
    gridGraph.remove_node(gridGraph.get_node(Position(3,1)))
    gridGraph.remove_node(gridGraph.get_node(Position(3,2)))
    gridGraph.remove_node(gridGraph.get_node(Position(8,5)))
    gridGraph.remove_node(gridGraph.get_node(Position(9,9)))    
    
    return gridGraph

