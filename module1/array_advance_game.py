def array_advance_game(array):
    furthest_reach=0
    last_index=len(array)-1
    i=0
    while i<=furthest_reach and furthest_reach<last_index:
        furthest_reach=max(furthest_reach,array[i]+i)
        i+=1
    return furthest_reach>=last_index
ar=[3,3,1,0,1,0,1]
print(array_advance_game(ar))

#method2
def array_advance_game(array):
    goal=len(array)-1
    for i in range(len(array)-2,-1,-1):
        if array[i]+i>=goal:
            goal=i
    return goal==0
a=[2,3,0,0,5]
print(array_advance_game(a))