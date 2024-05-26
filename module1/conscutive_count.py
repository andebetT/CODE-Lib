def consecutive_zeros(string):
    count = 0
    max_count = 0
    for i in range(len(string)):
        if string[i] == "0":
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

print(consecutive_zeros("1001100000000010001100000000000000000000"))
