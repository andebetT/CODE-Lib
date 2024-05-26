def add_without_plus_operator(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Test the function
num1 = 5
num2 = 7
result = add_without_plus_operator(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")


#this method used for if the numbers have negative value
def add_without_plus_operator(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = (carry & 0xFFFFFFFF) << 1 if carry < 0 else (carry >> 1)
    return a

# Test the function
num1 = -9
num2 = 5
result = add_without_plus_operator(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")




#solve linrar equation
a, b, c = 5, 9, 4
m, n, o = 7, 9, 4

temp = a * n - b * m

if n != 0:
    x = (c * n - b * o) / temp
    y = (a * o - m * c) / temp
    print("x =", x)
    print("y =", y)
else:
    print("The equation cannot be solved. Division by zero error.")

