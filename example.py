class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating nodes
drink = Node("Drink")
hot = Node("Hot")
cold = Node("Cold")

# Connecting nodes
drink.left = hot
drink.right = cold

tea = Node("Tea")
coffee = Node("Coffee")

hot.left = tea
hot.right = coffee

# Printing values
print(drink.value)        # Output: Drink
print(drink.left.value)   # Output: Hot