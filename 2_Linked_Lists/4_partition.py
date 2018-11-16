from utils import LinkedList

def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = nextNode

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None
    return ll

ll = LinkedList()
n = ll.append(55)
ll.append_multiple([82, 95, 20, 47, 37, 11, 42, 91, 6, 74])
ll.display()
print('Patition created at {}'.format(n.value))
ll = partition(ll, n.value)
ll.display()
