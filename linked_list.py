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


#ODD EVEN LINKED LIST
if head is None and head.next is None:
    print(head)
values = [], temp = head
while temp and temp.next:
    values.append(temp.val)
    temp = temp.next.next
temp = head.next
while temp and temp.next:
    values.append(temp.val)
    temp = temp.next.next
temp = head
index = 0
while temp is not None:
    temp.val = values[index]
    index+=1
    temp = temp.next
print(head)

#optimal choice change the links
if head is None or head.next is None:
    print(head)
odd = head
even = head.next
even_head = even
while even is not None and even.next is not None:
    odd.next = odd.next.next
    odd = odd.next
    even.next = even.next.next
    even = even.next
    odd.next = even.head
    print(head)

#remove nth node from the end of list

length = 0
temp = head
while temp is not None:
    length += 1
    temp = temp.next
if length == n:
    new_head = head.next
    del head
    print(new_head)
position_to_stop = length - n
temp = head
count = 0
while count<position_to_stop:
    temp=temp.next
    count+=1
temp.next = temp.next.next
print(head)

#optimal

slow = fast = head
for _ in range(n):
    fast = fast.next
if fast==None:
    print(head.next)
while fast.next is not None:
    slow = slow.next
    fast = fast.next
slow.next = slow.next.next
print(head)

#delete all occurences of a key
k = key = 2
if head.next is None and head.val == k:
    print(None)
temp = head
prev = None
new_head = head
while temp is not None:
    if temp.val == key:
       if prev is not None:
           temp.next.prev = prev
       if temp == new_head:
            new_head = new_head.next
prev = temp
temp = temp.next
print(new_head) 

#find pairs with given sum in DLL
target = 7
temp1 = head
result = []
while temp1 is not None:
    temp2 = temp1.next
    while temp2 is not None:
        if temp1.data + temp2.data == target:
            result.append([temp1.data, temp2.data])
        temp2 = temp2.next
    temp1 = temp1.next
print(result)

#optimal choice
my_set = set()
temp = head
result = []
while temp is not None:
    remaining = target - temp.data
    if remaining in my_set:
        result.append([remaining, temp.data])
    my_set.add(temp.data)
    temp = temp.next
print(result)

#more optimal choice
#sorted - use 2 pointer
result = []
left = head
right = head
while right is not None and right.next is not None:
    right = right.next
while left is not None and right is not None and left.data < right.data:
    total = left.data + right.data
    if total == target:
        result.append([left.data, right.data])
        left = left.next
        right = right.prev
    elif total < target:
        left = left.next
    else:
        right = right.prev
print(result)

#remove duplicates from DLL
if curr.prev == head:
    curr.prev = None
    head = curr
curr.prev.prev.next = curr
curr.prev = curr.prev.prev
