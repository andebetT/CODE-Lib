def maximum_profit(array):
    profit = 0
    minimum = array[0]
    for i in range(1, len(array)):
        minimum = min(minimum, array[i])
        profit = max(profit, array[i] - minimum)
    return profit


a = [7, 1, 5, 3, 6, 4]
print(maximum_profit(a))


def climb_star(star):
    prev1 = 1
    prev2 = 1
    for i in range(2, star + 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    return prev2


print(climb_star(6))


def last_start(arr, target):
    start = -1
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while target == arr[i + 1]:
                i += 1
            break
    return start, i


print(last_start([1, 2, 3, 3, 3, 3, 3, 4], 3))


def start_finsh(arrra, target):
    left = 0
    right = len(arrra) - 1
    start = -1
    last = -1
    while left <= right:
        middle = (left + right) // 2
        if arrra[middle] == target:
            start = middle
            right = middle - 1
        elif arrra[middle] < target:
            left += 1
        else:
            right -= 1
    left = 0
    right = len(arrra) - 1
    while left <= right:
        middle = (left + right) // 2
        if arrra[middle] == target:
            last = middle
            left = middle + 1
        elif arrra[middle] < target:
            left += 1
        else:
            right -= 1
    return start, last


print(start_finsh([1, 2, 3, 4, 4, 4, 4, 4, 5, 6], 4))




