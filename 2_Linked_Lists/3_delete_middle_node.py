from utils import LinkedList

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next

ll = LinkedList()
ll.append_multiple([1, 2, 3, 4])
middle_node = ll.append(5)
ll.append_multiple([6, 7, 8, 9])

ll.display()
delete_middle_node(middle_node)
ll.display()
