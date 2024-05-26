def furthest_reach(array):
    n=len(array)
    goal=n-1
    for i in range(n-2,-1,-1):
        if array[i]+i>=goal:
            goal=i
    return goal==0
#print(furthest_reach([2,3,0,0,5]))
#method_two
def furthest_reach(array):
    maximum_furthest=0
    i=0
    while i<=array[i] and maximum_furthest<len(array):
        maximum_furthest=max(maximum_furthest,i+array[i])
        i+=1

    return maximum_furthest==len(array)-1
print(furthest_reach([2,3,0,0,5]))
