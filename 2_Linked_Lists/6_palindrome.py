from utils import LinkedList

def palindrome_runner(ll):
    runner = current = ll.head
    stack = []
    while runner and runner.next:
        stack.append(current.value)
        current = current.next
        runner = runner.next.next

    if runner:
        current = current.next

    while current:
        top = stack.pop()
        if top != current.value:
            return False
        current = current.next

    return True

ll = LinkedList()
ll.append_multiple([1,2,3,4,3,2,1])
ll.display()

result = palindrome_runner(ll)
print(result)
