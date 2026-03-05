# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         #optimal approach
#         slow = head
#         fast = head

#         while fast and fast.next:
#             slow = slow.next          # move 1 step
#             fast = fast.next.next     # move 2 steps

#             if slow == fast:
#                 return True           # cycle found

#         return False                  # no cycle

#         #brute force approach
#         temp = head
#         my_set = set()
#         while temp is not None:
#             if temp in my_set:
#                 return True
#             my_set.add(temp)
#             temp = temp.next
#         return False