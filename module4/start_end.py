
def find_indices(arr, target):
    left = 0
    right = len(arr) - 1
    # Find the starting index of the target element
    start_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            start_index = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Find the ending index of the target element
    end_index = -1
    left = start_index
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            end_index = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return start_index, end_index

# Example usage
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
target = 3
start, end = find_indices(arr, target)
print("Starting index:", start)  # Output: 3
print("Ending index:", end)  # Output: 5
