def two_sum_hash_map(arr,target):
    d={}
    for i in range(len(arr)):
        if target-arr[i] in d.values():
            return d[target-arr[i]],arr[i]
        d[i]=arr[i]

    return None
print(two_sum_hash_map([-2,1,2,4,7,11],13))

def two_ponter(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]+arr[right]==target:
            return arr[left],arr[right]
        elif arr[left]+arr[right]>target:
            right-=1
        else:
            left+=1
print(two_ponter([-2,1,2,4,7,11],13))
