def find_two_sum(array,target):
    d={}
    if len(array)<=1:
        return False
    for i in range(len(array)):
        if target-array[i] in d:
            return d[target-array[i]],i
        else:
            d[array[i]]=i

m=[1,3,11,2,7]
print(find_two_sum(m,9))