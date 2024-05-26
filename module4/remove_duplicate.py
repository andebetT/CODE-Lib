#remove duplicate from the array
def remove_duplicate(array):
    n= len(array)
    pivot=0
    for i in range(0,n-1):
        if array[i]!=array[i+1]:
            array[pivot]=array[i]
            pivot+=1
    array[pivot]=array[n-1]
    return array[0:pivot+1]
print(remove_duplicate([1,1,2,2,3,4]))


def word_reversal(sentenece):
    new_sentence=" "
    sentenece=sentenece.split()
    print(sentenece)
    sentenece=sentenece[::-1]
    for i in sentenece:
        new_sentence+="".join(i)+" "
    return new_sentence
sen="my name is andebet tilahun"
print(word_reversal(sen))

