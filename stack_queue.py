from collections import deque

class MyStack:
    def __init__(self):
        # Using deque as the underlying queue structure
        self.queue = deque()

    def push(self, x: int) -> None:
        # 1. Append element to the back (enqueue)
        self.queue.append(x)
        # 2. Rotate the queue so the new element is at the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # 3. Remove and return the front element (dequeue)
        return self.queue.popleft()

    def top(self) -> int:
        # 4. Return the front element without removing it
        return self.queue[0]

    def empty(self) -> bool:
        # 5. Check if the queue is empty
        return len(self.queue) == 0


# Example usage:
obj = MyStack()
obj.push(10)
obj.push(20)

print(obj.pop())    # Output: 20
print(obj.top())    # Output: 10
print(obj.empty())  # Output: False