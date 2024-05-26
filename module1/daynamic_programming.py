#this program is used to find the number of wys of coin exchange
def coin_exchange(coins, amount):
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for j in range(1, amount + 1):
            if coins[i] >j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
    return dp[n - 1][amount]
c = [2, 3, 5, 10]
print(coin_exchange(c, 15))
#this program is used to find the minimum number of coins needed for a certain amount
def minimum_coin_exchange(coins, value):
    m = len(coins)
    arr = [[0] * (value + 1) for _ in range(m)]
    for i in range(m):
        arr[i][0] = 0
    for i in range(m):
        for j in range(1, value + 1):
            if coins[i] > j:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = min(arr[i - 1][j], 1 + arr[i][j - coins[i]])
    return arr[m - 1][value]
a = [1, 5, 6, 9]
print(minimum_coin_exchange(a, 10))
#this program is used to solve knapsack problem using daynamic programing
def knapsack(weights, profits, amount):
    n = len(weights)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    print(dp)
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], profits[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = n, amount
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    selected_items.reverse()
    return dp[n][amount], selected_items


weights = [3, 4, 6, 5]
profits = [2, 3, 1, 4]
amount = 10

max_profit, selected_items = knapsack(weights, profits, amount)
print("Maximum profit:", max_profit)
print("Selected items:", selected_items)
#finding the subsequence of a string
def find_subsequences(string):
    subsequences = ['']

    for char in string:
        subsequences += [subseq + char for subseq in subsequences]

    return subsequences


string = "abc"
all_subsequences = find_subsequences(string)

print(all_subsequences)
#for subseq in all_subsequences:
    #print(subseq)

