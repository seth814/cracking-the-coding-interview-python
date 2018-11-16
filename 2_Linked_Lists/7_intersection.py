from utils import LinkedList
from utils import Node

def intersection(ll_1, ll_2):
    if ll_1.tail is not ll_2.tail:
        return False

    shorter = ll_1 if ll_1.length < ll_2.length else ll_2
    longer = ll_1 if ll_1.length > ll_2.length else ll_2

    diff = longer.length - shorter.length

    short, long = shorter.head, longer.head

    for i in range(diff):
        long = long.next

    while short is not long:
        short = short.next
        long = long.next

    return long.value

ll_1 = LinkedList()
ll_2 = LinkedList()
ll_1.append_multiple([2,8,4,9,2])
ll_2.append_multiple([3,4,1])
node = Node(5)
ll_1.append(node)
ll_2.append(node)
node = Node(1)
ll_1.append(node)
ll_2.append(node)

ll_1.display()
ll_2.display()

result = intersection(ll_1, ll_2)
print(result)
