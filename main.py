import turtle
import queue
from graph import *

turtle.penup()
turtle.shape("circle")
turtle.Screen().setup(0.9,0.9)
turtle.speed(0)


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
noahGraph.grid_graph(Position(5,5))

start = noahGraph.get_node(Position(1,1))
end = noahGraph.get_node(Position(3,2))

visited = depthfirstsearch(noahGraph, start, end)

for v in visited:
    v.set_state("SEARCHED")


start.set_state("START")
end.set_state("END")

noahGraph.draw_graph()  
input()