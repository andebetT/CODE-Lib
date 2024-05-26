def all_equal(list1):
    if len(list1) <= 1:
        return True
    else:
        for i in range(len(list1)-1):
            if list1[i]!=list1[i+1]:
                return False
    return True
list1=[1,1,1,1]
print(all_equal(list1))