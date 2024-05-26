def count_change(string):
    string=string.lower()
    count=0
    for i in range(len(string)-1):
        if string[i]!=string[i+1]:
            count+=1
    return count
g="abbBba"
print(count_change(g))
