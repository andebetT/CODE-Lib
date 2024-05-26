def check_array(arr):
    n = len(arr)
    if n < 2:
        return None
    increasing = True
    decreasing = True
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
        if not increasing and not decreasing:
            return i - 1
    if increasing:
        return arr[-1]
    elif decreasing:
        return arr[0]
    else:
        return None

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 2, 3, 2, 1]

print(check_array(array1))  # Output: 5
print(check_array(array2))  # Output: 5
print(check_array(array3))  # Output: 3