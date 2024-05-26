def nearest_entries(ints, N, k):
    left = right = bisect_left(ints, N)  # Find the index of the element closest to N
    if right >= len(ints):  # If right is out of bounds, adjust it
        right = len(ints) - 1
    if left > 0:  # If left is greater than 0, adjust it
        left -= 1

    while left > 0 and right < len(ints) - 1 and k > 0:
        left -= 1
        k -= 1
        right += 1
        k -= 1

    while left > 0 and k > 0:
        left -= 1
        k -= 1

    while right < len(ints) - 1 and k > 0:
        right += 1
        k -= 1

    return ints[left:right+1]
ints = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = 4
k = 2
print(nearest_entries(ints, N, k))  # Output: [2, 3, 4, 5, 6]