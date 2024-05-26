def dictionary_revers(dictionary):
    new_dict={}
    for i in dictionary:
        if dictionary[i] not in new_dict:
            new_dict[dictionary[i]]=[i]
        else:
            new_dict[dictionary[i]].append(i)
    return new_dict



files={"input":"randy","code":"stan","output":"randy"}
print(dictionary_revers(files))