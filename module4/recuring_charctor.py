def recurring_char(input_str):
    char_set = set()
    for char in input_str:
        if char in char_set:
            return char
        char_set.add(char)
    return None
input_str = "interviewquery"
print(recurring_char(input_str))