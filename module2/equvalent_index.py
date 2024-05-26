def equivalent_index(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i:]):
            return i-1
    return -1
arr=[1,7,3,5,6,10]
print(equivalent_index(arr))