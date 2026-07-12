#remove Nth node from end of list
# def oddEvenList(head):
#     if head is None or head.next is None:
#         return head

#     values = []

#     temp = head
#     # collect odd nodes
#     while temp:
#         values.append(temp.val)
#         if temp.next is None:
#             break
#         temp = temp.next.next

#     temp = head.next
#     # collect even nodes
#     while temp:
#         values.append(temp.val)
#         if temp.next is None:
#             break
#         temp = temp.next.next

#     temp = head
#     i = 0
#     while temp:
#         temp.val = values[i]
#         i += 1
#         temp = temp.next

#     return head

#optimal solution
def oddEvenList(head):

    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head