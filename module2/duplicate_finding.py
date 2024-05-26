def find_duplicate(lst):
    s={}
    for i in range(len(lst)-1):
        if lst[i] not in s:
            s[lst[i]]=1
        else:
            s[lst[i]]+=1
    z=[]
    for i in s:
        if s[i]>1:
            z.append(i)
    return z
l=[1,2,1,3,4,3,3]
print(find_duplicate(l))