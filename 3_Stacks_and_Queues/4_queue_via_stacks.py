from utils import Stack

class QueueViaStacks():

    def __init__(self):
        self.in_stack = Stack(5)
        self.out_stack = Stack(5)

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.size == 0:
            while self.in_stack.size:
                self.out_stack.push(self.in_stack.pop())
            if self.out_stack.is_empty is True:
                raise IndexError("Can't dequeue from empty queue")
        return self.out_stack.pop()

queue = QueueViaStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
