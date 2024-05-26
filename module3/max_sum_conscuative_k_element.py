def finding_max_sum(array,k):
    total=sum(array[:k])
    max_sum=total
    for i in range(len(array)-k):
        total=total-array[i]
        total=total+array[i+k]
        max_sum=max(max_sum,total)
    return max_sum
a=[6,10,11,12,0]
print(finding_max_sum(a,3))