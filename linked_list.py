#reverse a linked list using stack
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

stack = []
temp = head

# Store values in stack
while temp is not None:
    stack.append(temp.val)
    temp = temp.next

# Replace values in reverse order
temp = head
while temp is not None:
    temp.val = stack.pop()
    temp = temp.next

# Print reversed linked list
temp = head
while temp:
    print(temp.val, end=" ")
    temp = temp.next
    
#optimal
if head.next is None:
    print(head)
curr = head
prev = None
while curr is not None:
    front = curr.next
    curr.next = prev
    curr.prev = front
print(prev)

if head.next is None:
    print(head)
curr = head
prev = None
while curr is not None:
    front = curr.next
    curr.next = prev
    curr.prev = front
print(prev)

#middle of the linkedlist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#middle of the linked list
#brute force approach

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Find length of linked list
n = 0
temp = head
while temp:
    n += 1
    temp = temp.next

# Move to the middle node
temp = head
for _ in range(n // 2):
    temp = temp.next

print(temp.val)

#tortoise hare approach
slow = head
fast = head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
print(slow.val)

#Reverse a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

temp = head
stack = []
while temp is not None:
    stack.append(temp.val)
    temp = temp.next
    temp = head
while temp is not None:
    e = stack.pop()
    temp.val = e
    temp = temp.next
print(head.val)

#optimal
temp = head
prev = None
while temp is not None:
    front = temp.next
    temp.next = prev
    prev = temp
    temp = front 
    

#FIND THE LL CYCLE - store the address of every node and put them in set if they found again cycle exist

temp = head
my_set = set()
while temp is not None:
    if temp in my_set:
        print(True)
    my_set.add(temp)
    temp = temp.next
print(False)

#optimal - use 2 pointer
slow = fast = head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        print(True)
print(False)

#starting point of the cycle
#optimal
slow = head
fast = head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        print(slow)
print(None)

#length of the cycle
#brute force
temp = head
travel = 0
my_set = set()
while temp is not None:
    if temp in my_set:
        print (travel - my_set[temp])
    my_set[temp] = travel
    travel += 1
    temp = temp.next
print(0)

#optimal
slow = fast = head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        slow = slow.next
        count = 1
        while slow != fast:
            slow = slow.next
            count += 1
        print(count)
print(0)