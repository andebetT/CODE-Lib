def singleNonDuplicate(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == nums[mid ^ 1]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Example usage
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
result = singleNonDuplicate(nums)
print(result)

def reverseWords(s):
    # Trim leading and trailing spaces
    s = s.strip()

    # Split the string into an array of words
    words = s.split()

    # Reverse the order of words
    words = words[::-1]

    # Join the reversed words with a single space separator
    reversed_string = ' '.join(words)

    return reversed_string
def roman_to_integer(string):
    d={}