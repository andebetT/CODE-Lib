def selection_sort(arr):
    for i in range(1,len(arr)-1):
        min_val=min(arr[i:])
        min_index=arr.index(min_val,i)
        arr[i],arr[min_index]= arr[min_index],arr[i]
    return arr
array=[56,3,2,2,78,6,0]
print(selection_sort(array))

#with out using built in min and max method
def sel_sort(lst):
    for i in range(len(lst)):
        smaller=lst[i]
        for j in range(i+1,len(lst)):
            if lst[j]<smaller:
                smaller=lst[j]
        ind=lst.index(smaller,i)
        if lst[i]!=lst[ind]:
            lst[i],lst[ind]=lst[ind],lst[i]
    return lst
l=[2,5,8,21,65,90]
print(sel_sort(l))

