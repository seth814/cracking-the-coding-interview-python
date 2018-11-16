class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

array = [i for i in range(1,11,1)]
print(array)

def minimal_bst_helper(array, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    value = array[mid]
    root = Node(value)
    root.left = minimal_bst_helper(array, start, mid-1)
    root.right = minimal_bst_helper(array, mid+1, end)
    return root


def create_minimal_bst(array):
    return minimal_bst_helper(array, 0, len(array)-1)


tree = create_minimal_bst(array)

stack = [tree]

while len(stack) > 0:
    node = stack.pop(0)
    if node:
        print(node.value)
    if node.left:
        stack.append(node.left)
    if node.right:
        stack.append(node.right)
