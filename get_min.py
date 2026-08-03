class MinStack:
    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if not self.items:
            self.items.append([val, val])
        else:
            current_min = min(self.items[-1][1], val)
            self.items.append([val, current_min])

    def pop(self) -> None:
        if self.items:
            self.items.pop()

    def top(self) -> int:
        if not self.items:
            return -1
        return self.items[-1][0]

    def getMin(self) -> int:
        if not self.items:
            return -1
        return self.items[-1][1]
    
obj = MinStack()

obj.push(5)
obj.push(7)
obj.push(2)
obj.push(10)
obj.push(8)
obj.push(15)

print(obj.getMin())   # 2

obj.push(1)
obj.push(18)

print(obj.top())      # 18
print(obj.getMin())   # 1

obj.pop()
obj.pop()

print(obj.getMin())   # 2