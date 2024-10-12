import pygame

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Route:
  def __init__(self, end, weight = 1):
    self.end = end
    self.weight = weight

class Node:
  offset = 20
  state ={
    "START" : "green",
    "END" : "red",
    "CURRENT" : "orange",
    "SEARCHED" : "blue",
    "PATH" : "yellow",
    "DEFAULT" : "black"
    
  } 
  def __init__(self, position):
    self.position = position
    self.connections = []
    self.state = "DEFAULT"
    self.distance = 1000

  def set_state(self, state):
    self.state = state
      
  def get_distance(self):
      return self.distance

  def set_distance(self, d):
      self.distance = d
      

  def __str__(self):
      return "node" + str(self.position.x) +  str(self.position.y)

  def draw_node(self, screen, mapscale):
    nodesize = 25
    screen_x = self.position.x * mapscale + Node.offset
    screen_y = self.position.y * mapscale + Node.offset
    pygame.draw.rect(screen, Node.state[self.state], pygame.Rect(screen_x-nodesize/2, screen_y-nodesize/2, nodesize, nodesize))
    font = pygame.font.Font(None, 20)
    #font_text = font.render((str(self.position.x) + ", " + str(self.position.y) + str(self.min_distance)),1,"white")
    font_text = font.render(str(self.distance),1,"white")      
    screen.blit(font_text, (self.position.x*mapscale+nodesize/2, self.position.y*mapscale+nodesize/2))
    

  def draw_node_connections(self, screen, mapscale):
    for c in self.connections:
        pygame.draw.line(screen, "black", (self.position.x*mapscale+Node.offset, self.position.y*mapscale+Node.offset), (c.end.position.x*mapscale+Node.offset, c.end.position.y*mapscale+Node.offset))
      

  def get_connections(self):
    return self.connections

  def clear_connections(self):
    self.connections = []

  def add_connections(self, connections):
    for c in connections:
      self.connections.append(c)
  def remove_connection(self, c):
      self.connections.remove(c)
  def has_connection(self, node):
    for n in self.connections:
      if n == node:
        return True
    return False

