def merge_sort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[0:mid]
        right_list=list1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i+=1
                k+=1
            else:
                list1[k]=right_list[j]
                k+=1
                j+=1
        while j<len(right_list):
            list1[k]=right_list[j]
            j+=1
            k+=1
        while i < len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1
    return list1
print(merge_sort([4,1,3,2,89,31]))
