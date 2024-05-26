import random
def modify(strings, k):
    for i in range(k):
        m = random.choice(strings)
        # print(m)
        n = random.choice("ABCDEFGHI")
        # print(n)
        new_strings = strings.replace(m, n)
    return new_strings


st = "andebet"
print(modify(st, 4))

