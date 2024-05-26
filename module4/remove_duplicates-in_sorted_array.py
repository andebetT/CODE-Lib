def remove_duplicate(array):
    pointer=0
    for i in range(len(array)-1):
        if array[i]!=array[i+1]:
            array[pointer]=array[i]
            pointer+=1
    array[pointer]=array[len(array)-1]
    return array[:pointer+1]
print(remove_duplicate([1,2,3,3,3,4,5,5,5,6,7]))