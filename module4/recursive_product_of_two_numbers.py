# this program is used to find the length of string in recursive method
def recursive_length(string):
    if len(string) == 0:
        return 0
    return 1 + recursive_length(string[1:])


print(recursive_length("andebet"))


# used to count number of consonant in string
def find_consonants(string):
    voul = ["a", "u", "e", "v", "o"]
    if len(string) == 0:
        return 0
    if string[0] not in voul and string[0].isalpha():
        return 1 + find_consonants(string[1:])
    else:
        return find_consonants(string[1:])


print(find_consonants("andebet"))


# this program is used to ind the product of two numbers using recursive function

def find_product(x, y):
    if y == 0:
        return 0
    else:
        return x + find_product(x, y - 1)


print(find_product(2000, 500))

