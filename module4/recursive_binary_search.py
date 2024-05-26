

def binary_search(list1, value, left, right):
    if left <= right:
        middle = (left + right) // 2
        if list1[middle] == value:
            return middle
        elif list1[middle] < value:
            return binary_search(list1, value, middle + 1, right)
        else:
            return binary_search(list1, value, left, middle - 1)

    return -1

a = [1, 2, 3, 5]
print(binary_search(a, 5, 0, len(a) - 1))

