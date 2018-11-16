from utils import LinkedList

def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll

ll = LinkedList()
ll.append_multiple([1,2,2,3,4,5,6,7,7,7,8,8,9])
ll.display()

ll = remove_dups(ll)
ll.display()
