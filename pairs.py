# temp1 = head
# result = []
# while temp1 is not None:
#     temp2 = temp1.next
#     while temp2 is not None:
#         if temp1.val + temp2.val == target:
#             result.append((temp1.val, temp2.val))
#         temp2 = temp2.next
#     temp1 = temp1.next
# print(result)

# #BETTER
# my_set = set()
# temp = head
# result = []
# while temp is not None:
#     remaining = target - temp.data
#     if remaining in my_set:
#         result.append((remaining, temp.data))
#     my_set.add(temp.data)
#     temp = temp.next
# print(result)

#optimal
# result = [],left = head, right = tail
# while left is not None and right is not None and left != right:
#     current_sum = left.data + right.data
#     if current_sum == target:
#         result.append((left.data, right.data))
#         left = left.next
#         right = right.prev
#     elif current_sum < target:
#         left = left.next
#     else:
#         right = right.prev
# print(result)

