def plus_one(array):
    array[-1]+=1
    for i in range(len(array)-1,0,-1):
        if array[i]!=10:
            break
        array[i]=0
        array[i-1]+=1
    if array[0]==10:
        array[0]=1
        array.append(0)
    return array

print(plus_one([9,9,9,9]))