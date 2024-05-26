def roman_to_number(string):
    i = 0
    n = len(string)
    sum = 0
    # using the I, V, X, L, C, D or M keys on your keyboard.
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    while i < n:
        if i < n - 1 and d[string[i]] < d[string[i + 1]]:
            sum += d[string[i + 1]] - d[string[i]]
            i += 2
        else:
            sum += d[string[i]]
            i += 1
    return sum


print(roman_to_number("IVIII"))




