def find_anagram(string1, string2):
    d = {}
    for i in string1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in string2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    for i in d:
        if d[i] != 0:
            return False
    return True


print(find_anagram("andebet", "denabet"))

