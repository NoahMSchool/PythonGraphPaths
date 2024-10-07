# import turtle
import pygame
import queue
from graph import *

pygame.init()
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
color = (200,200,200)
screen.fill(color)

def graphsearch(order, graph, start, end=None):
  order.put(start)
  visited = []
  camefrom = {start: None}
  found = False
  while not order.empty():
    current = order.get()
    visited.append(current)
    if current == end:
      found = True
      break
    for n in graph.get_node_connections(current):
      if n.end not in visited:
        camefrom[n.end] = current
        order.put(n.end)
  path = []
  if found:
    current = camefrom[end]
    while current != None:
      path.append(current)
      current = camefrom[current]
    path.reverse()
  return (visited, path)


def depthfirstsearch(graph, start, end=None):
  print("DFS")
  return graphsearch(queue.LifoQueue(), graph, start, end)


def breadthfirstsearch(graph, start, end=None):
  print("BFS")
  return graphsearch(queue.Queue(), graph, start, end)


noahGraph = Graph()
noahGraph.grid_graph(Position(10, 10))
noahGraph.remove_node(noahGraph.get_node(Position(3,0)))
noahGraph.remove_node(noahGraph.get_node(Position(3,1)))
noahGraph.remove_node(noahGraph.get_node(Position(3,2)))
noahGraph.remove_node(noahGraph.get_node(Position(3,3)))


start = noahGraph.get_node(Position(2, 2))
end = noahGraph.get_node(Position(9, 7))

(visited, path) = breadthfirstsearch(noahGraph, start, end)
for v in visited:
  v.set_state("SEARCHED")
for p in path:
  p.set_state("PATH")

start.set_state("START")
end.set_state("END")

noahGraph.draw_graph(screen, 50)
pygame.display.flip()
input()
