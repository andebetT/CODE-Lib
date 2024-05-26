def sum_pair_indices(array, target):
    dictionary={}
    for i in range(len(array)):
        if target-array[i] in dictionary:
            return dictionary[target-array[i]],i
        dictionary[array[i]]=i
    return -1
m=[1,2,3,4]
print(sum_pair_indices(m,5))