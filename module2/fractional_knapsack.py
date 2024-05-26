def fractional_knapsack(value, weight, capacity):
    ratio = [value / weight for value, weight in zip(value, weight)]
    # new_ratio=sorted(ratio,reverse=True)
    index = list(range(len(value)))
    index.sort(key=lambda i: ratio[i], reverse=True)

    fractional = [0] * len(value)
    max_val = 0
    for i in index:
        if weight[i] <= capacity:
            fractional[i] = 1
            max_val += value[i]
            capacity -= weight[i]
        else:
            fractional[i] = capacity / weight[i]
            max_val += value[i] * capacity / weight[i]
    return max_val, fractional


weight = [30, 50, 10, 70, 40]
value = [150, 100, 90, 140, 120]
capacity = 150
print(fractional_knapsack(value, weight, capacity))
