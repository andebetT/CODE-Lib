def longest_non_reapiting_sub_string(name):
    pointer1 = 0
    pointer2 = 0
    list1 = []
    for i in range(len(name)):
        if name[i] not in list1:
            list1.append(name[i])
        else:
            pointer1 = max(pointer1, len(list1))
            list1 = list1[pointer2+1:i+1]
            pointer2 = 0
    pointer1 = max(pointer1, len(list1))
    return pointer1

print(longest_non_reapiting_sub_string("astugonder"))