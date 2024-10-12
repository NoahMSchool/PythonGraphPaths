# import turtle
import pygame
import queue
from debug import Debug
from graph import *

pygame.init()
clock = pygame.time.Clock()

(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
color = (200,200,200)
screen.fill(color)

def frame(gameObjects, clock):
    for o in gameObjects:
        o.update(clock)
        o.draw(screen)
    clock.tick(20)
    pygame.display.flip()
    #input()

def graphsearch(order, graph, start, end=None):
  order.put(start)
  start.set_distance(0)
  visited = []
  camefrom = {start: None}
  found = False
  while not order.empty():
    current = order.get()
    current.set_state("CURRENT")
    visited.append(current)
    frame(gameObjects, clock)
    
    if current == end:
      found = True
      break
    for n in graph.get_node_connections(current):
      if n.end not in visited:
        visited.append(n.end)
        n.end.set_distance(current.get_distance()+1)
        camefrom[n.end] = current
        order.put(n.end)
        n.end.set_state("PATH")
        
    current.set_state("SEARCHED")
    frame(gameObjects, clock)

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

def get_grid_graph(gridsize):
    gridGraph = Graph()
    gridsize = 10
    
    for y in range(gridsize):
      for x in range(gridsize):
         gridGraph.add_node(Node(Position(x,y)))
    
    gridGraph.remove_node(gridGraph.get_node(Position(3,0)))
    gridGraph.remove_node(gridGraph.get_node(Position(3,1)))
    gridGraph.remove_node(gridGraph.get_node(Position(3,2)))
    gridGraph.remove_node(gridGraph.get_node(Position(3,3)))
    
    
    gridGraph.redo_grid_connections()
    return gridGraph

gameObjects = []
gameObjects.append(Debug())
gridGraph = get_grid_graph(10)
gameObjects.append(gridGraph)

start = gridGraph.get_node(Position(2, 2))
end = gridGraph.get_node(Position(6, 6))
(visited, path) = breadthfirstsearch(gridGraph, start, end)


for v in visited:
  v.set_state("SEARCHED")
for p in path:
  p.set_state("PATH")
start.set_state("START")
end.set_state("END")


frame(gameObjects, clock)
input()
