def recursive_fun(list1):
    if len(list1) == 1:
        return list1[0]
    return list1[0] + recursive_fun(list1[1:])


n = [1, 2, 3, 4, 5, 6, 8]
print(recursive_fun(n))

#sum of digits of a number using recursive
def sum_digits(number):
    if number==0:
        return 0
    return number%10 +sum_digits(number//10)
print(sum_digits(234))



s={1,}


