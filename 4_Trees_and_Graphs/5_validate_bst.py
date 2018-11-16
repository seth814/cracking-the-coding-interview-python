class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


def check_bst_recursive(root,
                        lower_bound=-float('inf'),
                        upper_bound=float('inf')):
    if root is None:
        return True

    if (root.value > upper_bound or root.value <= lower_bound):
        return False

    return (check_bst_recursive(root.left, lower_bound, root.value)
            and check_bst_recursive(root.right, root.value, upper_bound))


def check_bst_iterative(root):
    if root is None:
        return True

    stack = [(root, -float('inf'), float('inf'))]
    while len(stack) > 0:
        node, lower_bound, upper_bound = stack.pop()
        
        if node.value <= lower_bound or node.value > upper_bound:
            return False

        if node.left:
            stack.append((node.left, lower_bound, node.value))
        if node.right:
            stack.append((node.right, node.value, upper_bound))
    return True


n_5 = Node(5)
n_2 = Node(2)
n_8 = Node(8)
n_1 = Node(1)
n_3 = Node(3)
n_6 = Node(6)
n_9 = Node(9)
n_4 = Node(4)
n_7 = Node(7)
n_10 = Node(10)

# same bst from 4.2 (minimal tree)
# depth 1
n_5.left = n_2
n_5.right = n_8
# depth 2
n_2.left = n_1
n_2.right = n_3
n_8.left = n_6
n_8.right = n_9
# depth 3
n_3.right = n_4
n_6.right = n_7
n_9.right = n_10

result = check_bst_recursive(n_5)
print(result)

result = check_bst_iterative(n_5)
print(result)
