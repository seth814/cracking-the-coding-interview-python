class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lca_helper(root, n1, n2, v):

    if root is None:
        return None

    if root.value == n1:
        v[0] = True
        return root

    if root.value == n2:
        v[1] = True
        return root

    left_lca = lca_helper(root.left, n1, n2, v)
    right_lca = lca_helper(root.right, n1, n2, v)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca

def find(root, n):
    if root is None:
        return False

    if (root.value == n or find(root.left, n) or find(root.right, n)):
        return True

    return False

def find_lca(root, n1, n2):

    v = [False, False]

    lca = lca_helper(root, n1, n2, v)

    both_exist = v[0] and v[1]
    check_n1 = v[1] and find(lca, n1)
    check_n2 = v[0] and find(lca, n2)
    if (both_exist or check_n1 or check_n2):
        return lca

    return None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

lca = find_lca(root, 4, 5)
print(lca.value)
lca = find_lca(root, 4, 6)
print(lca.value)
lca = find_lca(root, 4, 10)
print(lca)
