def binary_search_iterative(array,key):
    left=0
    right=len(array)-1
    while left<=right:
        middle=(left+right)//2
        if array[middle]==key:
            return middle
        elif array[middle]<key:
            left=middle+1
        else:
            right-=1
    return None
arr=[1,2,3,4,5,6]
#print(binary_search_iterative(arr,3))


def binary_search_recursive(array, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary_search_recursive(array, mid + 1, right, target)
        else:
            return binary_search_recursive(array, left, mid - 1, target)
    return -1

print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 0, 7, 9))
