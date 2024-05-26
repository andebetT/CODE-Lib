def diseruim_cheek(number):
    new_num = str(number)
    digit = sum(int(i) ** (index + 1) for index, i in enumerate(new_num))
    if digit == number:
        return True
    return False

print(diseruim_cheek(89))


def num_cheek(num1):
    n = str(num1)
    d = sum(int(i) for i in n)
    return num1 % d == 0

print(num_cheek(18))


def self_deviding(number):
    m = str(number)
    for i in m:
        if int(i) == 0 or number % int(i) != 0:
            return False
    return True


print(self_deviding(36))
for j in range(1, 20):
    if self_deviding(j):
        print(j)


# method2
def is_self_dividing(num):
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit == 0 or num % digit != 0:
            return False
        temp //= 10
    return True


def find_self_dividing_numbers(start, end):
    self_dividing_numbers = []
    for num in range(start, end + 1):
        if is_self_dividing(num):
            self_dividing_numbers.append(num)
    return self_dividing_numbers



