# finding the minimum in sorted rotated array
def find_min(array):
    left = 0
    right = len(array) - 1
    while left <right:
        middle = (left + right) // 2
        if array[middle] > array[right]:
            left = middle + 1
        else:
            right = middle
    return array[left]


print(find_min([4, 5, 6, 7, 1, 2, 3]))


def find_max(array):
    left = 0
    right = len(array) - 1
    while left < right:
        middle = (left + right) // 2
        if array[middle] < array[right]:
            right = middle - 1
        else:
            left = middle
    return array[right]


print(find_max([4, 5, 6, 7, 1, 2, 3]))

