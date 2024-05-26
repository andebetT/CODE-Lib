#finding the substring of a string
def find_substring(string):
    for i in range(len(string)):
        j=i
        while j<len(string)+1:
            print(string[i:j])
            j+=1
d="ANDEBET"
print(find_substring(d))