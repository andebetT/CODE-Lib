#finding intersection of two sorted array
def intersection(array1,array2):
    x=len(array1)
    y=len(array2)
    i=0
    j=0
    list=[]
    while i<x and j<y:
        if array1[i]==array2[j]:
            if array1[i]!=array1[i-1] and i>0:
                list.append(array1[i])
                i+=1
                j+=1
        elif array1[i]<array2[j]:
            i+=1
        else:

            j+=1
    return list
array1=[1,2,3,4]
array2=[2,3]
print(intersection(array1,array2))

