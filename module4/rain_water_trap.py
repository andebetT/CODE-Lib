def rain_water_trap(arr):
    size=len(arr)
    left=size*[0]
    right=size*[0]
    left_max=arr[0]
    right_max=arr[-1]
    sum=0
    for i in range(1,size):
        if left_max<arr[i]:
            left_max=arr[i]
            left[i]=left_max
        else:
            left[i]=left_max
    print(left)
    for i in range(size-1,-1,-1):
        if right_max<arr[i]:
            right_max=arr[i]
            right[i]=right_max
        else:
            right[i]=right_max
    print(right)
    for i in range(size):
        sum+=min(left[i],right[i])-arr[i]
    return sum
a=[0,3,1,3,2,5]
print(a)
print(rain_water_trap(a))
