class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # Enqueue Operation: Add to the end (O(1))
    def enqueue(self, item):
        self.items.append(item)

    # Dequeue Operation: Remove from the front (O(N))
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    # Front Operation: Get the first element (O(1))
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    # Rear Operation: Get the last element (O(1))
    def rear(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)


# --- Example Usage ---
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(f"Front element: {q.front()}")
print(f"Rear element: {q.rear()}")
print(f"Dequeued: {q.dequeue()}")
print(f"Queue size: {q.size()}")