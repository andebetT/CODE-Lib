def palindrome_making(string, target):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            if string[left] == target:
                string = string[:left] + string[left + 1:]
            elif string[right] == target:
                string = string[:right] + string[right + 1:]
            else:
                print("palindrome is not possible")
                return None
        right -= 1
        left += 1
    return string

string = "racecar"
target_char = "e"
print(palindrome_making(string, target_char))