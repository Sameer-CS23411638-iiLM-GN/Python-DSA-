class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class MyQueue:
    def __init__(self):
        self.front = None  # Points to first element
        self.rear = None   # Points to last element

    def enqueue(self, x):
        new_node = Node(x)

        # If queue is empty
        if self.rear is None:
            self.front = self.rear = new_node
            return

        # Insert at rear
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return -1  # Queue underflow

        temp = self.front
        self.front = self.front.next

        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None  # Queue becomes empty

        return temp.data

    def peek(self):
        if self.front is None:
            return -1
        return self.front.data

    def isEmpty(self):
        return self.front is None


# Example usage
q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek())      # 10
print(q.dequeue())   # 10
print(q.peek())      # 20
print(q.isEmpty())   # False