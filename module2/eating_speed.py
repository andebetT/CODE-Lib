import math
def mineatingspeed(array,h):
    def k_works(k):
        hours=0
        for i in array:
            hours+=math.ceil(i/k)
        return hours<=h
    left=1
    right=max(array)
    while left<right:
        k=(left+right)//2
        if k_works(k):
            right=k
        else:
            left=k+1
    return right
print(mineatingspeed([3,6,7,11],8))
