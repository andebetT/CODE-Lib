def find_number_of_rotation(rotted_array):
    left = 0
    right = len(rotted_array) - 1
    while left <= right:
        mid = (left+right) // 2
        if rotted_array[mid] < rotted_array[mid-1] and mid > 0:
            return mid
        elif rotted_array[mid] < rotted_array[right]:
            right = mid - 1
        else:
            left = mid + 1
rotated=[5,6,9,0,0,0,0,2,3,4]
print(find_number_of_rotation(rotated))
#this code is used to find the number of rotation of if the array have reapeted element
def find_number_of_rotation(rotated_array):
    left = 0
    right = len(rotated_array) - 1

    while left <= right:
        mid = (left + right) // 2

        if rotated_array[mid] < rotated_array[mid - 1] and mid > 0:
            return mid

        if rotated_array[left] == rotated_array[mid] and rotated_array[mid] == rotated_array[right]:
            if rotated_array[left] > rotated_array[left + 1]:
                return left + 1
            left += 1
            right -= 1
        elif rotated_array[mid] < rotated_array[right]:
            right = mid - 1
        else:
            left = mid + 1

    return 0

rotated = [2,2,2,1,1,2,2,2]
print(find_number_of_rotation(rotated))
def find_target(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return None
# Rotated sorted array: [5, 6, 9, 0, 2, 3, 4]
arr = [5, 6, 9, 0, 2, 3, 4]
target = 2
result = find_target(arr, target)
print(result)
