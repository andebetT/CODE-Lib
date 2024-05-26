def search_insert_position(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        middle=(left+right)//2
        if array[middle]==target:
            return middle
        elif array[middle]<target:
            left=middle+1
        else:
            right=middle-1
    return left
a=[1,3,5,6]
print(search_insert_position(a,2))