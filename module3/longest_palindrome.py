def longest_palindrome(string):
    if len(string) < 2:
        return string

    start = 0
    max_length = 1
    for i in range(len(string)):
        # Check for odd-length palindromes
        left = i - 1
        right = i + 1
        while left >= 0 and right < len(string) and string[left] == string[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

        # Check for even-length palindromes
        left = i
        right = i + 1
        while left >= 0 and right < len(string) and string[left] == string[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    return string[start:start + max_length]

