def group_anagram(list1):
    d={}
    for i in range(len(list1)):
        word="".join(sorted(list1[i]))
        if word not in d:
            d[word]=[list1[i]]
        else:
            d[word].append(list1[i])
    return d.values()
list2=["cat","dog","tca","act"]
print(group_anagram(list2))

