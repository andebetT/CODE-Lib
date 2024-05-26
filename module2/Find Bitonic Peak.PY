#linear search
def Find_Bitonic_Peak(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            return array[i]
    return None
a=[1,2,3,4,5,4,3,2,1]
print(Find_Bitonic_Peak(a))
#method2 binary search
def find_bitonic_peak(ar):
    left=0
    right=len(ar)-1
    #there must be at least 3 elements to achive bitonic sequence
    if len(ar)<3:
        return None
    while left<=right:
        middle=(left+right)//2
        mid_left=ar[middle-1] if middle-1>0 else float("-inf")
        mid_right=ar[middle+1] if middle+1<len(ar) else float("inf")
        if mid_left<ar[middle] and mid_right>ar[middle]:
            left=middle+1
        elif mid_left>ar[middle] and ar[middle]>ar[right]:
            right=middle-1
        elif mid_left<ar[middle] and mid_right<ar[middle]:
            return ar[middle]
    return None
a=[1,2,3,4,5,4,3,2,1]
print(find_bitonic_peak(a))


