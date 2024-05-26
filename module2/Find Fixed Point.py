#this program is used for to find the element which is equal to its index
#method1:using linear search
def Find_Fixed_Point(array):
    for i in range(len(array)):
        if array[i]==i:
            return array[i]
    return None
a=[-10,-5,0,3,7]
print(Find_Fixed_Point(a))

#method2:using binary search
def find_fixed_point(arr):
    left=0
    right=len(arr)-1
    while left<=right:
        middle=(left+right)//2
        if arr[middle]<middle:
            left=middle+1
        elif arr[middle]>middle:
            right=middle-1
        else:
            return middle
    return None
print(find_fixed_point(a))
