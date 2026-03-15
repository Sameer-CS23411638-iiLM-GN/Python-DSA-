def removeDuplicates(head):
    temp = head

    while temp and temp.next:
        if temp.val == temp.next.val:
            node = temp.next
            temp.next = node.next

            if node.next:
                node.next.prev = temp
        else:
            temp = temp.next

    return head