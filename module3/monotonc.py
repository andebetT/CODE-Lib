def check_array_order(arr):
    increasing = True
    decreasing = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            increasing = False
        if arr[i] < arr[i + 1]:
            decreasing = False

    if increasing:
        print("Increasing array")
    elif decreasing:
        print("Decreasing array")
    else:
        print("Neither increasing nor decreasing array")


# Example usage
array1 = [1, 2, 3, 4, 5]
check_array_order(array1)  # Output: Increasing array

array2 = [5, 4, 3, 2, 1]
check_array_order(array2)  # Output: Decreasing array

array3 = [1, 2, 3, 2, 4]
check_array_order(array3)  # Output: Neither increasing nor decreasing array


a="a b  "
a=a.rstrip()
print(len(a))


def ArrayChallenge(arr):
    increasing=True
    decreasing=True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            increasing=False
        if arr[i]<arr[i+1]:
            decreasing=False
        else:
            break
    if increasing or decreasing:
        return -1
    return i
print(ArrayChallenge([1, 2, 4, 6]))

if number<=1:
    return number
return fun(n-4)+n(n-2)