
def dictionary(list1):
    d={}
    for i in range(len(list1)):
        word="".join(sorted(list1[i]))
        if word not in d:
            d[word]=[i]
        else:
            d[word].append(i)
    return d

a=["cat","dog","god","tca","act"]
print(dictionary(a))