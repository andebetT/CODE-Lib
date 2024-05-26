def finding_happy_number(number):
    list1=[]
    string=str(number)
    while string not in list1:
        list1.append(string)
        total=0
        for i in string:
            i=int(i)
            total+=i**2
        if total==1:
            return True
        string=str(total)
    return False
print(finding_happy_number(19))
'''def reverse_str(name):
    n=""
    for i in range(len(name)-1,-1,-1):
        n+=name[i]
    return n
print(reverse_str("andebet"))'''