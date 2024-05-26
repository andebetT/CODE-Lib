def knapsack_greedy(values, weights, capacity):
    # Create a list of (value, weight, index) tuples
    items = [(v, w, i) for i, (v, w) in enumerate(zip(values, weights))]
    # Sort the items in descending order of value-to-weight ratio
    print(items)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    selected_items = []
    remaining_capacity = capacity
    for item in items:
        value, weight, index = item
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            selected_items.append(index)
            remaining_capacity -= weight
        else:
            if remaining_capacity>0:
                total_value+=value/remaining_capacity

    return total_value, selected_items
# Example usage
values = [5, 10, 15,7,8,9,4]
weights = [1,3,5,4,1,3,2]
capacity = 15
max_value, selected_items = knapsack_greedy(values, weights, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
