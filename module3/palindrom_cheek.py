def palindromine(string):
    last=len(string)-1
    first=0
    while first<last:
        if string[first]!=string[last]:
            return False
        first+=1
        last-=1
    return True
st="AABBAA"
print(palindromine(st))