def wave_array(array):
    m=len(array)
    for i in range(0,m,2):
        if i>0 and array[i-1]>array[i]:
            array[i-1],array[i]=array[i],array[i-1]
        if i<m-1 and array[i]<array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
    return array
arr=[1,2,6,4,5]
print(wave_array(arr))

