from utils import LinkedList

def reverse(ll):

    previous = None
    current = ll.head
    next_node = current.next

    while current:
        current.next = previous

        previous = current
        current = next_node
        if next_node:
            next_node = next_node.next

    ll.head = previous
    return ll

ll = LinkedList()
ll.add_multiple([1,2,3,4,5,6,7,8,9])
ll.display()
ll = reverse(ll)
ll.display()
