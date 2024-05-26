
def max_sum_subarray(arrr):
    current_sum=0
    max_sum=arrr[0]
    for i in arrr:
        current_sum=current_sum+i
        if current_sum<0:
            current_sum=0
        max_sum=max(max_sum,current_sum)
    return max_sum
a=[-2,7,-3,4]
print(max_sum_subarray(a))
def summing(ar,m):
    sum=0
    po=0
    for i in range(len(ar)+1):
        if sum==m:
            break
        else:
            sum+=ar[i]
            while sum>m:
                sum=sum-ar[po]
                po+=1
    return ar[po:i]
b=[23,1,4,20,3,10,5]
print(summing(b,23))



