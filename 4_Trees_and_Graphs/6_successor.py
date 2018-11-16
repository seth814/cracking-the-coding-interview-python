class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.value)


def in_order_traversal(node):
    if node is None:
        return None

    # successor is in our right tree
    if node.right is not None:
        return left_most_child(node.right)
    # successor is one of the ancestors
    else:
        child = node
        parent = child.parent
        while (parent is not None and parent.left is not child):
            child = parent
            parent = parent.parent
        return parent


def left_most_child(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node


n_1 = Node(1)
n_2 = Node(2)
n_3 = Node(3)
n_4 = Node(4)
n_5 = Node(5)
n_6 = Node(6)
n_7 = Node(7)

#       6
#      / \
#     2   7
#    / \
#   1   4
#      / \
#     3   5

# depth 0
n_6.left = n_2
n_6.right = n_7
# depth 1
n_2.left = n_1
n_2.right = n_4
n_2.parent = n_6
n_7.parent = n_6
# depth 2
n_4.left = n_3
n_4.right = n_5
n_1.parent = n_2
n_4.parent = n_2
# depth 3
n_3.parent = n_4
n_5.parent = n_4

nodes = [n_1, n_2, n_3, n_4, n_5, n_6, n_7]
# each call the in_order_traversal
# should return the successor node in bst

for n in nodes:
    result = in_order_traversal(n)
    print(result)
