class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self):
        values = [str(x) for x in self]
        values = ', '.join(values)
        return values

    def append(self, value):
        if isinstance(value, Node):
            self.helper(value)
        else:
            self.helper(Node(value))

        return self.tail

    def helper(self, node):
        if self.head is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1

    def append_multiple(self, iterable):
        for i in iterable:
            self.append(i)

    def display(self):
        print(self)
