def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n  # Initialize dp array with all 1s

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
nums = [10, 9, 2, 5, 3, 3, 7, 101, 18]
print(longest_increasing_subsequence(nums))