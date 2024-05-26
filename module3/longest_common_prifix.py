def longest_common_prefix(list1):
    n = len(list1)
    i = 0
    min_length = float("inf")

    for s in list1:
        min_length = min(min_length, len(s))

    while i < min_length:
        for s in list1[1:]:
            if s[i] != list1[0][i]:
                return list1[0][:i]
        i += 1

    if i == 0:
        return ""

    return list1[0][:i]


l = ["flower", "flight", "flow"]
print(longest_common_prefix(l))