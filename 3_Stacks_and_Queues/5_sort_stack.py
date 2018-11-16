from utils import Stack

def sort_stack(stack):

    s1 = stack
    s2 = Stack(s1.size)

    while(s1.is_empty() != True):
        temp = s1.pop()
        while(s2.is_empty() != True and s2.peek() > temp):
            s1.push(s2.pop())
        s2.push(temp)

    return s2

stack = Stack(10)
stack.push(1)
stack.push(3)
stack.push(7)
stack.push(4)
stack.push(8)
stack.push(2)
stack.push(9)
stack.push(5)
stack.push(6)

sorted_stack = sort_stack(stack)

temp = []
while sorted_stack.is_empty() != True:
    temp.append(sorted_stack.pop())
