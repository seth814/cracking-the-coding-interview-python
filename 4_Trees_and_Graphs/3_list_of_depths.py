class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


def helper(node, lists, depth):

    if node is None:
        return

    if len(lists) == depth:
        list = []
        lists.append(list)
    else:
        list = lists[depth]
    list.append(node)

    helper(node.left, lists, depth+1)
    helper(node.right, lists, depth+1)


def list_of_nodes_recursive(root):

    lists = []
    helper(root, lists, 0)
    return lists


def list_of_nodes_iterative(root):

    nodes = []
    stack = []
    if root is not None:
        stack.append(root)

    while len(stack) > 0:
        current = stack.pop(0)
        nodes.append(current)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return nodes


n_1 = Node(1)
n_2 = Node(2)
n_3 = Node(3)
n_4 = Node(4)
n_5 = Node(5)
n_6 = Node(6)
n_7 = Node(7)

n_1.left = n_2
n_1.right = n_3
n_2.left = n_4
n_2.right = n_5
n_3.left = n_6
n_3.right = n_7

tree = n_1
ll = list_of_nodes_recursive(tree)
print(ll)

ll = list_of_nodes_iterative(tree)
print(ll)
