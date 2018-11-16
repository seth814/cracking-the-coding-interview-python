class Node:

    def __init__(self, value):
        self.value = value
        self.neighbors = set()

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

visited = set()
stack = [a]
while len(stack) > 0:
    node = stack.pop(0)
    visited.add(node)
    print(node.value)

    for neighbor in node.neighbors:
        if neighbor not in visited:
            stack.append(neighbor)

