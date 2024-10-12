import pygame
from node import *

class Graph:
  def __init__(self):
    self.nodes = []
  def draw(self, screen):
    self.draw_graph(screen, 50)
  def update(self, clock):
      pass
  def draw_graph(self, screen, mapscale):
    for n in self.nodes:
      n.draw_node_connections(screen, mapscale)
    for n in self.nodes:
      n.draw_node(screen, mapscale)

  def return_nodes(self):
    return self.nodes

  def add_node(self, Node):
    self.nodes.append(Node)

  def remove_node(self, Node):
    self.nodes.remove(Node)
    self.redo_grid_connections()
  
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

  def redo_grid_connections(self):
      for n in self.nodes:
        self.grid_connect(n)
  
  def grid_connect(self, n):
    n.clear_connections()
    square = [(1,0),(0,1),(-1,0),(0,-1)]
    diagonals = [(1,1),(1,-1),(-1,1),(-1,-1)]
    directions = square + diagonals
    for d in directions:
        target = self.get_node(Position(n.position.x + d[0], n.position.y + d[1]))
        if self.has_node(target):
            n.add_connections([Route(target, 1)])


