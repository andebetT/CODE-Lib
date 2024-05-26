def gcd(int_list):
    if len(int_list) < 2:
        return None

    def find_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    result = int_list[0]
    for i in range(1, len(int_list)):
        result = find_gcd(result, int_list[i])

    return result
l=[4,8,16,24]
print(gcd(l))

