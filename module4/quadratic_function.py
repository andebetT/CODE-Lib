#write python program to solve quadratic eqution
import math
a= float(input("enter cofficient a:"))
b=float(input("enter cofficient b:"))
c=float(input("enter cofficient c:"))
discriminant=b**2-4*a*c
if discriminant>0:
    print("the equation have tow real and distinct roots")
    root1=-b+math.sqrt(discriminant)/2*a
    root2=-b-math.sqrt(discriminant)/2*a
    print(f"root1 is:{root1}")
    print(f"root2 is:{root2}")
elif discriminant==0:
    print("the equation have only one real rooot")
    root=-b/(2*a)
else:
    print("the equation have complex roots")
    real_part_root=-b/(2*a)
    imaginary_part_root=math.sqrt(abs(discriminant))/(2*a)
    print(f"root1 is:{real_part_root}+{imaginary_part_root}i")
    print(f"root2 is :{real_part_root}-{imaginary_part_root}i")
#python program ro cheek prime
def prime_chek(num):
    for i in range(2,num+1):
        if num%i==0:
            return False
    return True
n=int(input("please enter the number"))
if prime_chek(n):
    print("the number is prime")
else:
    print("the number is not prime")
#sum of natural number
m=100
sum=0
for i in range(1,101):
    sum+=i
print(sum)
print(100*101//2)
