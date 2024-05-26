def max_sequence_of_ones(arr, k):
    left = 0
    zeros_count = 0
    max_ones_count = 0
    max_ones_start = 0

    for right in range(len(arr)):
        if arr[right] == 0:
            zeros_count += 1

        if zeros_count > k:
            if arr[left] == 0:
                zeros_count -= 1
            left += 1

        ones_count = right - left + 1
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            max_ones_start = left

    return arr[max_ones_start:max_ones_start + max_ones_count]


# Example usage:
arr = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
k = 1
max_ones = max_sequence_of_ones(arr, k)
print("Maximum sequence of 1's:", max_ones)
