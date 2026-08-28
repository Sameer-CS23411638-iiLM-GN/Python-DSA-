class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # 1. Transfer all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # 2. Insert new element to s1
        self.s1.append(x)

        # 3. Transfer all elements back from s2 to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        if not self.s1:
            return -1
        return self.s1.pop()

    def peek(self) -> int:
        if not self.s1:
            return -1
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0


# Example usage:
obj = MyQueue()
obj.push(10)
obj.push(20)

print(obj.peek())   # Output: 10
print(obj.pop())    # Output: 10
print(obj.empty())  # Output: False