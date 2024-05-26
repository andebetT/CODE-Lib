def gas_station(gas,cost):
    remaining=0
    prev_remaining=0
    candidate=0
    if len(gas)==1 and len(cost)==1:
        if gas[0]==cost[0]:
            return 0
        return -1
    for i in range(len(gas)):
        remaining+=gas[i]-cost[i]
        if remaining<0:
            candidate=i+1
            prev_remaining+=remaining
            remaining=0
    if candidate==len(gas)or remaining+prev_remaining<0:
        return -1
    else:
        return candidate

gas=[1,5,3,3,5,3,1,3,4,5]
cost=[5,2,2,8,2,4,2,5,1,2]
print(gas_station(gas,cost))
