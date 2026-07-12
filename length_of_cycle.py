# #brute force
# travel = 0
# temp = head
# my_dict = {}

# while temp is not None:
#     if temp in my_dict:
#         return travel - my_dict[temp]
#     else:
#         my_dict[temp] = travel

#     temp = temp.next
#     travel += 1

# return 0

# #optimal solution
# slow = head
# fast = head

# while fast is not None and fast.next is not None:
#     slow = slow.next
#     fast = fast.next.next

#     if slow == fast:
#         count = 1
#         slow = slow.next

#         while slow != fast:
#             slow = slow.next
#             count += 1

#         return count

# return 0