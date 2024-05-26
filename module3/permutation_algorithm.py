def permutation_algorithm(string,picket=""):
    if len(string)==0:
        print(picket)
    else:
        for i in range(len(string)):
            letter=string[i]
            front=string[0:i]
            back=string[i+1:]
            together=front+back
            permutation_algorithm(together,letter+picket)
print(permutation_algorithm("ABC",""))