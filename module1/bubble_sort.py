def bubbble_sort(arr):
    for j in range(len(arr)):
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
array=[20,14,25,16,45,60,12]
print(bubbble_sort(array))
