class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: Detect if cycle exists
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head

                # Step 2: Find start of cycle
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None