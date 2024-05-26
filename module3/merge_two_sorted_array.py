def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = 0  # index for arr1
    j = 0  # index for arr2
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Append remaining elements from arr1, if any
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # Append remaining elements from arr2, if any
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    m=len(merged_array)
    middle=m//2
    if m%2==0:
        return sum(merged_array[middle]+merged_array[middle-1])/2
    return merged_array[middle]







# Example usage
array1 = [1,2,3]
array2 = [2, 5,6]
def merge(nums1, m, nums2, n):
    i = m - 1  # Pointer for nums1
    j = n - 1  # Pointer for nums2
    k = m + n - 1  # Pointer for the merged array
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Copy the remaining elements from nums2 to nums1 if any
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return  nums1
*a,b=[1,2,3,4]
print(b)