def reverseDLL(head):
    stack = []
    
    temp = head
    
    # Push all values into stack
    while temp is not None:
        stack.append(temp.val)
        temp = temp.next
    
    temp = head
    
    # Pop values and assign back
    while temp is not None:
        temp.val = stack.pop()
        temp = temp.next
    
    return head

#optimal solution

# if head.next is not None:
#     return head
# curr=head
# prev=None
# while curr is not None:
#     front=curr.next
#     curr.next=prev
#     curr.prev=front
#     prev=curr
#     curr=front
# return head
