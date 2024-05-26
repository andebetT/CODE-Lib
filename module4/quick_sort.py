#this code is used for sort ascending order by considering the first element as rhe piviot element
def pivot_position(list1,first, last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right
def quick_sort(list1,first,last):
    if first<last:
        p=pivot_position(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
    return list1
list1=[56,26,93,17,31,44]
n=len(list1)
print(quick_sort(list1,0,n-1))
# for decemding oreder of arreangemenet we use this code
def pivot_position(list1,first, last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]>=pivot:
            left+=1
        while left<=right and list1[right]<=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right
def quick_sort(list1,first,last):
    if first<last:
        p=pivot_position(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
    return list1
list1=[56,26,93,17,31,44]
n=len(list1)
print(quick_sort(list1,0,n-1))
#by using the last element as the pivot
def pivot_position(list1,first, last):
    pivot=list1[last]
    left=first
    right=last-1
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[last],list1[left]=list1[left],list1[last]
    return left
def quick_sort(list1,first,last):
    if first<last:
        p=pivot_position(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
    return list1
list1=[56,26,93,17,31,44]
n=len(list1)
print(quick_sort(list1,0,n-1))
#for selcting random element as pivot
import random
def pivot_position(list1,first, last):
    ran=random.randint(first,last)
    list1[ran],list1[last]=list1[last],list1[ran]
    pivot=list1[last]
    left=first
    right=last-1
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[last],list1[left]=list1[left],list1[last]
    return left
def quick_sort(list1,first,last):
    if first<last:
        p=pivot_position(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
    return list1
list1=[56,26,93,17,31,44]
n=len(list1)
print(quick_sort(list1,0,n-1))
#using the mieadin of
import statistics
def pivot_position(list1,first, last):
    low=list1[first]
    high=list1[last]
    mid=(last+first)//2
    pivot=statistics.median([low,list1[mid],high])
    if pivot==low:
        pivot_index=first
    elif pivot==high:
        pivot_index=last
    else:
        pivot_index=mid
    list1[first],list1[pivot_index]=list1[pivot_index],list1[first]
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right
def quick_sort(list1,first,last):
    if first<last:
        p=pivot_position(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
    return list1
list1=[56,26,93,17,31,44]
n=len(list1)
print(quick_sort(list1,0,n-1))


