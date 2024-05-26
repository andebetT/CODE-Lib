def find_single_element(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Example usage
arr = [1, 2, 3, 4, 2, 3, 1]
single_element = find_single_element(arr)
print("The element that is repeated once is:", single_element)