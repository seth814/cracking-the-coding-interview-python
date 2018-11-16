class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


def check_height(node):
    if node is None:
        return 0
    
    left_height = check_height(node.left)
    if left_height == -1:
        return -1
    right_height = check_height(node.right)
    if right_height == -1:
        return -1

    height_diff = abs(left_height - right_height)
    if height_diff > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


def is_balanced_recursive(root):
    return check_height(root) > -1


def is_balanced_iterative(root):
    if root is None:
        return True

    depths = []
    stack = []
    # tuple in stack:
    # node and depth of node
    stack.append((root, 0))

    while len(stack):
        node, depth = stack.pop()

        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)

            if ((len(depths) > 2) or
                    (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                return False

        else:
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
    return True


n_1 = Node(1)
n_2 = Node(2)
n_3 = Node(3)
n_4 = Node(4)
n_5 = Node(5)
n_6 = Node(6)

# adding node 6 creates an unbalanced tree
n_1.left = n_2
n_1.right = n_3
n_3.left = n_4
n_3.right = n_5
n_4.right = n_6

tree = n_1
result = is_balanced_recursive(tree)
print(result)

result = is_balanced_iterative(tree)
print(result)
