def find_first_entry(arr,target):
    i=0
    while arr[i]<target:
        i+=1
    return i
print(find_first_entry([8,8,9,10],8))


def Find_First_Entry_in_List_with_Duplicates(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]<target:
            left=mid+1
        elif array[mid]>target:
            right=mid-1
        else:
            if array[mid-1]!=target or mid-1<0:
                return mid
    return None
p=[5,5,5,5,6]
print(Find_First_Entry_in_List_with_Duplicates(p,5))