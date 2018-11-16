from utils import LinkedList
from utils import Node

def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        print(slow.value, fast.value)
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    print(slow.value, fast.value)
    if fast is None or fast.next is None:
        return None

    print('---')
    slow = ll.head
    while fast != slow:
        print(slow.value, fast.value)
        fast = fast.next
        slow = slow.next
    print(slow.value, fast.value)

    print(fast.value)

ll = LinkedList()
ll.append_multiple([1,2,3,4])
node = Node(5)
ll.append_multiple([node, Node(6), Node(7), Node(8), Node(9), node])

loop_detection(ll)
