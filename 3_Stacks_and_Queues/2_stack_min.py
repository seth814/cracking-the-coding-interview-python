class Stack:

    def __init__(self, stacksize):
        self.stack_capacity = stacksize
        self.array = [None] * stacksize
        self.size = 0
        self.min_stack = [None]

    def push(self, item):
        if self.is_full():
            raise Exception('Stack is full')
        if self.min_stack[-1] is None or item < self.min_stack[-1]:
            self.min_stack.append(item)
        self.size += 1
        self.array[self.index_of_top()] = item

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        value = self.array[self.index_of_top()]
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        self.array[self.index_of_top()] = None
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.array[self.index_of_top()]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.stack_capacity

    def index_of_top(self):
        return self.size - 1

    def get_min(self):
        return self.min_stack[-1]

stack = Stack(5)
stack.push(9)
print(stack.get_min())
stack.push(7)
print(stack.get_min())
stack.push(2)
print(stack.get_min())
stack.pop()
print(stack.get_min())
stack.pop()
print(stack.get_min())
stack.pop()
print(stack.get_min())
