import turtle
import queue

turtle.penup()
turtle.shape("circle")
turtle.speed(10)
mapscale = 50

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Route:
  def __init__(self, end, weight = 1):
    self.end = end
    self.weight = weight

class Node:

  def __init__(self, position):
    self.position = position
    self.connections = []

  def __str__(self):
      return "node" + str(self.position.x) +  str(self.position.y)

  def draw_node(self):
    screen_x = self.position.x * mapscale
    screen_y = self.position.y * mapscale
    turtle.goto(screen_x, screen_y)
    turtle.stamp()

  def draw_node_connections(self):
    for c in self.connections:
      screen_x = self.position.x * mapscale
      screen_y = self.position.y * mapscale
      turtle.goto(screen_x, screen_y)
      turtle.pendown()
      screen_x = c.end.position.x * mapscale
      screen_y = c.end.position.y * mapscale
      turtle.goto(screen_x, screen_y)
      turtle.penup()

  def get_connections(self):
    return self.connections

  def add_connections(self, connections):
    for c in connections:
      self.connections.append(c)

  def update_connections(self, Graph):
    #self.connections = intersection(self.connections, Graph.return_nodes())
    for c in self.connections:
      found = False
      for n in Graph.return_nodes:
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

  def draw_graph(self):
    for n in self.nodes:
      n.draw_node()
      n.draw_node_connections()

  def return_nodes(self):
    return self.nodes

  def add_node(self, Node):
    self.nodes.append(Node)

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

    for n in self.nodes:

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



def graphsearch(order, graph, start, end = None):
    order.put(start)
    visited = []
    while not order.empty():
        current = order.get()
        print(current)
        visited.append(current)
        if current == end:
            return visited
        for n in graph.get_node_connections(current):
            if n.end not in visited:
                order.put(n.end)
    return visited
def depthfirstsearch(graph, start, end = None):
    print("DFS")
    return graphsearch(queue.LifoQueue(), graph, start, end)
def breadthfirstsearch(graph, start, end = None):
    print("BFS")
    return graphsearch(queue.Queue(), graph, start, end)




noahGraph = Graph()
noahGraph.grid_graph(Position(3,3))
noahGraph.draw_graph()  

start = noahGraph.get_node(Position(1,1))
end = noahGraph.get_node(Position(2,1))

visited = breadthfirstsearch(noahGraph, start, end)

for v in visited:
    print(v)
