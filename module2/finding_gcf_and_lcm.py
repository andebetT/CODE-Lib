def lcm_finding(a,b):
    if a<b:
        grater=b
    else:
        grater=a
    while True:
        if grater%a==0 and grater%b==0:
            return grater
        grater+=1
print(lcm_finding(10,3))
#gcf
def gcf_finding(num1,num2):
    while num2!=0:
        num1,num2=num2,num1%num2
    return num1
print(gcf_finding(10,5))