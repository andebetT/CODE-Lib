#finding the frequencey of an elemnt in a sorted array using binary search
def find_frequency(arr, element):
    count = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            count += 1
            # Check for additional occurrences on the left side
            i = mid - 1
            while i >= left and arr[i] == element:
                count += 1
                i -= 1
            # Check for additional occurrences on the right side
            i = mid + 1
            while i <= right and arr[i] == element:
                count += 1
                i += 1

            return count

        elif arr[mid] < element:
            left = mid + 1

        else:
            right = mid - 1

    return count


# Example usage
array = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]
element = 5
frequency = find_frequency(array, element)
print(f"The frequency of {element} in the array is: {frequency}")


#this program is used to find a target element in a sorted square matrix using binary search
def find_target(matrix,target):
    if not matrix or len(matrix[0]) == 0:
        return False
    rows =len(matrix)
    columns=len(matrix[0])
    row =0
    col=columns-1
    while row<rows and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            row+=1
        else:
            col-=1
matrix=[
    [1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 60],[70, 80, 90, 100]]
print(find_target(matrix,16))

def find_peak_element(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            # If the middle element is greater than the next element,
            # a peak element may exist in the left half
            right = mid
        else:
            # If the middle element is less than or equal to the next element,
            # a peak element may exist in the right half
            left = mid + 1

    # At the end of the loop, left and right will be pointing to the peak element
    return left
print(find_peak_element([1,2,3,1]))


def count_zeros(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the mid index corresponds to the transition from ones to zeros
        if arr[mid] == 0 and (mid == 0 or arr[mid - 1] == 1):
            return len(arr) - mid

        # If the mid element is 1, move to the right half of the array
        if arr[mid] == 1:
            left = mid + 1
        # If the mid element is 0, move to the left half of the array
        else:
            right = mid - 1

    return 0

def find_kth_element(arr1, arr2, k):
    m, n = len(arr1), len(arr2)
    i, j = 0, 0

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            k -= 1
            if k == 0:
                return arr1[i]
            i += 1
        else:
            k -= 1
            if k == 0:
                return arr2[j]
            j += 1

    # If we reach here, it means one of the arrays has been exhausted
    while i < m:
        k -= 1
        if k == 0:
            return arr1[i]
        i += 1

    while j < n:
        k -= 1
        if k == 0:
            return arr2[j]
        j += 1

    return None  # k is out of range of the combined arrays


# Example usage
array1 = [2, 4, 6, 8, 10]
array2 = [1, 3, 5, 7, 9]
k = 5

result = find_kth_element(array1, array2, k)
print("Element at kth position:", result)


def find_median(arr1, arr2):
    merged = []
    i, j = 0, 0
    m, n = len(arr1), len(arr2)

    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < m:
        merged.append(arr1[i])
        i += 1

    while j < n:
        merged.append(arr2[j])
        j += 1

    total_len = m + n
    if total_len % 2 == 0:
        mid = total_len // 2
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        mid = total_len // 2
        return merged[mid]


# Example usage
array1 = [1, 3, 5]
array2 = [2, 4, 6, 8, 10]

median = find_median(array1, array2)
print("Median of the sorted arrays:", median)

def minimum_change(cents):
    sum=0
    i=0
    count=0
    list_coins=[25,10,5,1]
    while i<len(list_coins):
        while cents-sum>=list_coins[i]:
            sum+=list_coins[i]
            count+=1
        i+=1
    return count
print(minimum_change(73))

d={"a":3,"b":1,"c":4}
d={key:val for key,val in sorted(d.items(),key=lambda d:d[1],reverse=True)}
print(d)




import random

def random_number(x, y=0, count=1):
    if count == 1:
        return x

    # Probability of selecting the new value
    probability = 1 / count

    # Randomly decide whether to select the new value or keep the previous value
    if random.random() < probability:
        return x
    else:
        return y
x = 10  # New value from the stream
y = 5  # Previously selected value
count = 2  # Size of the stream

selected_number = random_number(x, y, count)
print(selected_number)


def draw_isosceles_triangle(h, b):
    if b % 2 == 0 or h <= 0 or b <= 0:
        return None

    triangle = []
    for i in range(h):
        row = []
        for j in range(b):
            if j >= (b // 2 - i) and j <= (b // 2 + i):
                row.append(1)
            else:
                row.append(0)
        triangle.append(row)

    return triangle
print(draw_isosceles_triangle(3,9))

