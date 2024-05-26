values = [5, 10, 15,7,8,9,4]
weights = [1,3,5,4,1,3,2]
ratio_items = [[v/w] for v, w in (zip(values, weights))]
print(ratio_items)
idx=list(range(len(values)))
sorted_idx=sorted(idx,key=lambda x:ratio_items[x],reverse=True)
print(sorted_idx)
maximum=15
max_profit=0
for i in sorted_idx:
    if weights[i]<=maximum:
        max_profit+=values[i]
        maximum=maximum-weights[i]
    else:
        if maximum>0:
            max_profit+=maximum/values[i]
print(max_profit)

