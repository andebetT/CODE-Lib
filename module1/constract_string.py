# this code is used to evaluate we can constract first string  using leters in the second code with out reapiting
def constract(string1, string2):
    letters = {}
    for i in string2:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    for j in string1:
        if j not in letters:
            return False
        if letters[j] == 1:
            del letters[j]
        else:
            letters[j] -= 1
    return True


print(constract("aa", "aab"))


