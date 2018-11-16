class MultiStack:
    
    def __init__(self, stacksize):
        self.numstacks = 3
        self.stack_capacity = stacksize
        self.array = [None] * (self.numstacks * stacksize)
        self.sizes = [0] * self.numstacks
        
    def push(self, item, stacknum):
        if self.is_full(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.index_of_top(stacknum)] = item
        
    def pop(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.index_of_top(stacknum)]
        self.array[self.index_of_top(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value
    
    def peek(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.index_of_top(stacknum)]
    
    def is_empty(self, stacknum):
        return self.sizes[stacknum] == 0
    
    def is_full(self, stacknum):
        return self.sizes[stacknum] == self.stack_capacity
    
    def index_of_top(self, stacknum):
        offset = stacknum * self.stack_capacity
        return offset + self.sizes[stacknum] - 1
    
stack = MultiStack(2)
print(stack.is_empty(1))
stack.push(3, 1)
print(stack.peek(1))
print(stack.is_empty(1))
stack.push(2, 1)
print(stack.peek(1))
print(stack.pop(1))
print(stack.peek(1))
stack.push(3, 1)
