def counting_common(string1, string2):
    count = 0
    for i in string1:
        if i in string2:
            count += 1
    return count


s1 = "aAAA"
s2 = "aA"
print(counting_common(s1, s2))

s3 = set(s2)
count = 0
for s in s1:
    if s in s3:
        count += 1
print(count)

