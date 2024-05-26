def Find_Closest_Number(arr,target):
    if len(arr)==0:
        return None
    if len(arr)==1:
        return arr[0]
    left=0
    right=len(arr)-1
    closest_num=None
    min_difference=float("inf")
    while left<=right:
        middle=(left+right)//2
        if middle+1<len(arr):
            min_difference_right=abs(arr[middle+1]-target)
        if middle>0:
            min_difference_left=abs(arr[middle-1]-target)
        if min_difference_left<min_difference:
            min_difference=min_difference_left
            closest_num=arr[middle-1]
        if min_difference_right<min_difference:
            min_difference=min_difference_right
            closest_num=arr[middle+1]
        if arr[middle]<target:
            left=middle+1
        elif arr[middle]>target:
            right=middle-1
        else:
            return arr[middle]
    return closest_num
numbers=[1,2,4,5,6,6,8,9]
print(Find_Closest_Number(numbers,11))

