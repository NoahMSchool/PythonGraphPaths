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
    nodesize = 40
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

  def update_connections(self, Graph):
    #self.connections = intersection(self.connections, Graph.return_nodes())
    for c in self.connections:
      found = False
      for n in Graph.return_nodes():
        if c == n:
          found = True
      if found == False:
        self.connections.remove(c)

  def has_connection(self, node):
    for n in self.connections:
      if n == node:
        return True
    return False

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

  def grid_graph(self, gridsize):
    for y in range(gridsize.y):
      for x in range(gridsize.x):
        self.add_node(Node(Position(x,y)))
    self.redo_grid_connections()
  
  def redo_grid_connections(self):
      for n in self.nodes:
        self.grid_connect(n)
    
  def grid_connect(self, n):
    n.clear_connections()
    right = self.get_node(Position(n.position.x+1, n.position.y))
    left = self.get_node(Position(n.position.x-1, n.position.y))
    up = self.get_node(Position(n.position.x, n.position.y+1))
    down = self.get_node(Position(n.position.x, n.position.y-1))
    if self.has_node(right):
      n.add_connections([Route(right)])
    if self.has_node(left):
      n.add_connections([Route(left, 1)])
    if self.has_node(up):
      n.add_connections([Route(up, 1)])
    if self.has_node(down):
      n.add_connections([Route(down, 1)])


