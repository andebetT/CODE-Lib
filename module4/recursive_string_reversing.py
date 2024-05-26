def reversing(list222):
    if len(list222)==0:
        return ""
    return list222[len(list222)-1]+reversing(list222[0:len(list222)-1])
c="hello"
print(reversing(c))

def array_product(arr):
    if len(arr)==0:
        return 0
    if len(arr)==1:
        return arr[0]
    return arr[0]*array_product(arr[1:])
print(array_product([3,6,8,9,2,1]))