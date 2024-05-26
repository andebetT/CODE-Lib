#this program is used to find the lengerth of the last word after space
def length_lastword(word):
    n=len(word)
    i=n-1
    while word[i]==" ":
        i=-1
    letter_count=0
    for j in range(i+1):
        if word[j]!=" ":
            letter_count+=1
        else:
            letter_count=0
    return letter_count
print(length_lastword("hello worlde"))

