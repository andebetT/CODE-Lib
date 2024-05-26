#duplicate letter count
def count_duplicate(string):
    dictionary={}
    for i in string:
        if i.lower() not in dictionary:
            dictionary[i.lower()]=1
        else:
            dictionary[i.lower()]+=1
    count=0
    for i in dictionary:
        if dictionary[i]>1:
            count+=1
    return count
print(count_duplicate("ANDEBEandebet"))

def direduction(arr):
    dict1={}
    for i in arr:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    print(dict1)
print(direduction(["e","w","n","s"]))
val="1234"
v=list(val)
print(sorted(v,reverse=True))
n="".join(v)
print(n)
def bit_count(number):
    bit=""
    count=0
    while number>0:
        bit+=str(number%2)
        number=number//2
    for i in bit:
        if i =="1":
            count+=1
    return count
print(bit_count(1234))
print(bin(12345))
num=["180","90"]
print(sorted(num))
