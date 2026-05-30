class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractionalKnapsack(arr, capacity):
    # Sort by value/weight ratio in descending order
    arr.sort(key=lambda item: item.value / item.weight, reverse=True)

    final_value = 0.0
    current_weight = 0

    for item in arr:
        if current_weight + item.weight <= capacity:
            current_weight += item.weight
            final_value += item.value
        else:
            remaining_weight = capacity - current_weight
            final_value += item.value * (remaining_weight / item.weight)
            break  # Knapsack is full

    return final_value


# Example
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50

print("Maximum value:", fractionalKnapsack(arr, capacity))