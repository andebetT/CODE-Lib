#this program is used for finding the power of a number using greeddey algorithim
def power_finding(x,n):
    if n==0:
        return 1
    if n%2==0:
        even_half=power_finding(x,n//2)
        return even_half*even_half
    else:
        odd_half=power_finding(x,(n-1)/2)
        return odd_half*odd_half*x
print(power_finding(2,8))