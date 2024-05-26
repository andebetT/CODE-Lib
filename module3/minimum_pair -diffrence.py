def min_distance(V):
    V.sort()
    min_diff = float('inf')
    for i in range(len(V) - 1):
        diff = abs(V[i] - V[i + 1])
        if diff < min_diff:
            min_diff = diff

    pairs = []
    # Find pairs with the minimum absolute difference
    for i in range(len(V) - 1):
        if abs(V[i] - V[i + 1]) == min_diff:
            pairs.append([V[i], V[i + 1]])

    return pairs
v = [3, 12, 126, 44, 52, 57, 144, 61, 68, 72, 122]
print(min_distance(v))  # Output: [[57, 61], [68, 72], [122, 126]]