# #brute force approach
# while temp is not None:
#   if temp.val == key:
#     if prev is not None:
#       prev.next = temp.next
#     if temp.next is not None:
#       temp.next.prev = prev
#     if temp == new_head:
#         new_head = new_head.next
#     prev = temp
#     temp = temp.next
# return new_head
  