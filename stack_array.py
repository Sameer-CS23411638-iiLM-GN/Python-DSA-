class Stack:
    def __init__(self):
        self.items = []  # Internal array to store elements

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the top item from the stack."""
        if self.is_empty():
            return "Stack is Empty, cannot pop"
        return self.items.pop()

    def top(self):
        """Returns the top item without removing it."""
        if self.is_empty():
            return "Stack is Empty"
        return self.items[-1]

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.items)

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return len(self.items) == 0


# --- Example Usage ---
stack = Stack()
stack.push(2)
stack.push(5)
stack.push(7)

print(f"Top element: {stack.top()}")
print(f"Popped element: {stack.pop()}")
print(f"Stack size: {stack.size()}")