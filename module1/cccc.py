def coun(string):
    count=1
    st=""
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            count+=1
        st+=str(count)+string[i]
    return st
print(coun("3322251"))
