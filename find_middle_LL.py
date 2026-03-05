#brute force approach
class LinkedList:
#odd
    def find_middle(self):
        n = 0
        temp = self.head

        while temp is not None:
            n += 1
            temp = temp.next

        temp = self.head

        for i in range(n // 2):
            temp = temp.next

        print(temp.data)
#even
    def find_middle(self):
        n = 0
        temp = self.head

        while temp is not None:
            n += 1
            temp = temp.next

        temp = self.head

        for i in range(n // 2):
            temp = temp.next

        print(temp.data)
#optimal approach
# slow = head
# fast = head
# while fast is not None and fast.next is not None:
#     slow = slow.next
#     fast = fast.next.next
# print(slow.data)
