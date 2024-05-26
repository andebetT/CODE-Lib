#used to find duplicate element using constant space
# "Majority Vote Algorithm" or the "Boyer-Moore Majority Vote Algorithm."
def duplicate_find(array):
    count=0
    candidate=None
    for i in array:
        if count==0:
            candidate=i
        count+=1 if candidate==i else -1
    return candidate
print(duplicate_find([1,3,4,2,2]))


def search_insert_position(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]>target:
            right=mid-1
        elif array[mid]==target:
            return mid
        else:
            left+=1
    return left
print(search_insert_position([1,3,4,2,2],4))


def sort_colours(array):
    red_count=0
    white_count=0
    for i in array:
        if i==0:
            red_count+=1
        elif i==1:
            white_count+=1
    return [0]*red_count+[1]*white_count+[2]*(len(array)-(white_count+red_count))
print(sort_colours([2,0,2,1,1,0]))

#Find First and Last Position of Element in Sorted Array
#method1 using linear search
def find_first_last(arr,target):
    start=-1
    for i in range(len(arr)):
        if arr[i]==target:
            start=i
            while i<len(arr) and arr[i]==arr[i+1]:
                i+=1
            return start,i
    return [-1,-1]
print(find_first_last([5,7,7,8,8,10],8))



#method2 using binary search
def find_first_last(arr,target):
    left=0
    right=len(arr)-1
    start=-1
    end=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            start=mid
            right=mid-1
        elif arr[mid]>target:
            right-=1
        else:
            left+=1
    left=start
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            end=mid
            left=mid+1
        elif arr[mid]>target:
            right-=1
        else:
            left+=1
    return start,end
print(find_first_last([5,7,7,8,8,10],8))







