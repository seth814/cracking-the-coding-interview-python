class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def subtree_equality(t2, t1):
    if t2 is None and t1 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t2.value == t1.value:
        return subtree_equality(t2.left, t1.left) and subtree_equality(t2.right, t1.right)
    return False


def check_subtree(t2, t1):
    if t1 is None or t2 is None:
        return False
    if t1.value == t2.value:
        if subtree_equality(t2, t1):
            return True
    return check_subtree(t2, t1.left) or check_subtree(t2, t1.right)


# t1 >> t2
# check if t2 is a subtree of t1

