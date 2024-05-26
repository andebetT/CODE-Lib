#linear search program
def linear_search(lst,target):
    for i in range(len(lst)-1):
        if lst[i]==target:
            return i

m=[1,2,3,4,5]
print(linear_search(m,4))
