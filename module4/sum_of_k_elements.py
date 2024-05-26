def count_triplets(nums, k):
    nums.sort()  # Sort the array in ascending order
    count = 0
    # Fix the first element of the triplet
    for i in range(len(nums) - 2):
        left = i + 1  # Pointer to the second element
        right = len(nums) - 1  # Pointer to the third element
        while left < right:
            # Check if the triplet sums up to k
            if nums[i] + nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            # If the sum is less than k, move the left pointer to the right
            elif nums[i] + nums[left] + nums[right] < k:
                left += 1
            # If the sum is greater than k, move the right pointer to the left
            else:
                right -= 1

    return count
nums1 = [1, 2, 3, 4, 5]
k1 = 6
print(count_triplets(nums1, k1))  # Output: 1

nums2 = [10, 10, 20, 30, 40]
k2 = 60
print(count_triplets(nums2, k2))  # Output: 3