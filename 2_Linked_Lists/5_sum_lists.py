from utils import LinkedList

def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.append(result % 10)
        carry = result // 10

    if carry:
        ll.append(carry)

    return ll

ll_a = LinkedList()
ll_a.append_multiple([6, 1, 7])
ll_b = LinkedList()
ll_b.append_multiple([2, 9, 5])
ll_a.display()
ll_b.display()
ll_sum = sum_lists(ll_a, ll_b)
ll_sum.display()
