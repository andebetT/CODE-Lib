def reversing_string(string):
    s=list(string)
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    m="".join(s)
    return m
m="123456"
print(reversing_string(m))