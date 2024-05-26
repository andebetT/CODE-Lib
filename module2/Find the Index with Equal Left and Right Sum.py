def equivalent_index(nums):
    for i in range(len(nums)):
        if sum(nums[:i+1])==sum(nums[i+1:]):
            return i
    return -1
nums = [1, 7, 3, 5, 6]
print(equivalent_index(nums))



import random
continues_random_function = random.random
m=continues_random_function()
print(m)