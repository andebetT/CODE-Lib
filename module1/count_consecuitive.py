def max_consecutive(array):
    s = set(array)
    count = 0
    for i in array:
        if i-1 not in s:
            current = 1
            while i+1 in s:
                current += 1
                i += 1
            count = max(current, count)
    return count

print(max_consecutive([100, 4, 200, 1, 2, 3]))