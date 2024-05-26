from math import ceil
def perfect_square(number):
    left=1
    right=ceil(number/2)
    while left<=right:
        mid=(left+right)//2
        if mid*mid==number:
            return True
    return False
print(perfect_square(16))
