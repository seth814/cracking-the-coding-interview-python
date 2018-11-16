from utils import LinkedList

def kth_to_last(ll, k):
    if k <= 0:
        raise(AttributeError('Set k to a value greater than 0'))

    current = runner = ll.head
    for i in range(k):
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current.value

ll = LinkedList()
ll.append_multiple([1,2,3,4,5,6,7,8,9])
kth_to_last = kth_to_last(ll, 2)
print(kth_to_last)
