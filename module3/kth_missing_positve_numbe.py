def find_Kth_Positive_missing_number(arr, k):
    missingCount = 0
    currentNumber = 1

    for num in arr:
        while currentNumber < num:
            missingCount += 1
            if missingCount == k:
                return currentNumber
            currentNumber += 1
        currentNumber += 1

    while missingCount < k:
        missingCount += 1
        if missingCount == k:
            return currentNumber
        currentNumber += 1

    return currentNumber

a = [2, 3, 4, 7, 11]
k = 5
result = find_Kth_Positive_missing_number(a, k)
print(result)