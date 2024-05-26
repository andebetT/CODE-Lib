def fibonacci_itration(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2,n+1):
            a, b = b, a + b
        return b

fib_5 = fibonacci_itration(8)
print(fib_5)

def fibonancci_recursion(number):
    if number<=1:
        return number
    return fibonancci_recursion(number-1)+fibonancci_recursion(number-2)
print(fibonancci_recursion(8))
