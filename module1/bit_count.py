def countSetBits(n):
    sum = 0
    for j in range(1, n + 1):
        while j > 0:
            reminder = j % 2
            sum += reminder
            j = j // 2

    return sum % 10 ** 7


print(countSetBits(5))

