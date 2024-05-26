def validPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Check if excluding s[left] results in a palindrome
            without_left = s[:left] + s[left + 1 :]

            # Check if excluding s[right] results in a palindrome
            without_right = s[:right] + s[right + 1 :]

            return without_left == without_left[::-1] or without_right == without_right[::-1]

        left += 1
        right -= 1

    return True  # The string is already a palindrome

# Example usage:
s = "aba"
print(validPalindrome(s))  # Output: True

m="andebet"
for i in range(len(m)-1,-1,-1):
    print(m[i])