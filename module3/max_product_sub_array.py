def max_product_subarray(arr):
    current_max=arr[0]
    current_min=arr[0]
    previous_max=arr[0]
    previous_min=arr[0]
    result=arr[0]
    for i in range(1,len(arr)):
        current_max=max(previous_max*arr[i],previous_min*arr[i],arr[i])
        current_min=min(previous_max*arr[i],previous_min*arr[i],arr[i])
        result=max(current_max,result)
        previous_max=current_max
        previous_min=current_min
    return result
array=[-6,4,-5,8,-10,0,8]
print(max_product_subarray(array))