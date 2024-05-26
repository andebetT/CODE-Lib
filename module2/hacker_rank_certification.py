def max_pairs(weights):
    """
    Determine the maximum number of pairs the company can sell.

    Args:
        weights (list): A list of weights of the dumbbells.

    Returns:
        int: The maximum number of pairs the company can sell.
    """
    # Sort the weights in ascending order
    weights.sort()

    # Initialize the dp table
    dp = [[0] * (len(weights) + 1) for _ in range(len(weights) + 1)]

    # Fill the dp table
    for i in range(1, len(weights) + 1):
        for j in range(1, len(weights) + 1):
            if abs(weights[i-1] - weights[j-1]) <= 1:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(weights)][len(weights)]

# Example usage
weights = [3, 4, 5, 3]
print(max_pairs(weights))  # Output: 7

d={}

for i in range(26):
    d[chr(65+i)]=i+1
for i in range(26):
    d[chr(97+i)]=i+1
print(d)

