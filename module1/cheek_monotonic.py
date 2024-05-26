def monotonic_array(arr):
    increasing=True
    decreasing=True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            increasing=False
        if arr[i+1]>arr[i]:
            decreasing=False
    return decreasing or increasing
print(monotonic_array([1,2,3,4,5]))

