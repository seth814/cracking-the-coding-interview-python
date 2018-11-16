from enum import Enum

class State(Enum):

    unvisited = 1
    visited = 2
    visiting = 3

class Node:

    def __init__(self, value):
        self.value = value
        self.neighbors = set()
        self.state = State.unvisited


def eval_route(graph, start, end):

    start.state = State.visiting
    stack = [start]
    while len(stack) > 0:
        node = stack.pop(0)
        print(node.value)

        if node:
            for neighbor in node.neighbors:
                if neighbor.state is State.unvisited:
                    if neighbor is end:
                        return True
                    else:
                        node.state = State.visiting
                        stack.append(neighbor)

            node.state = State.visited
    return False


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.neighbors.add(b)
b.neighbors.update([c, d])
d.neighbors.update([e, g])
e.neighbors.add(f)
g.neighbors.add(h)
h.neighbors.add(e)

graph = [a, b, c, d, e, f, g, h]
print(eval_route(graph, a, h))
