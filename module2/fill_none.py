def fill_none(input_list):
    filled_list = []
    previous_value = 0  # Assume the previous entry was 0 if the first entry is None
    for value in input_list:
        if value is not None:
            previous_value = value  # Update the most recent non-None value
        filled_list.append(previous_value)

    return filled_list
input_list = [1, 2, None, None, 4, 5, None]
print(fill_none(input_list))  # Output: [1, 2, 2, 2, 4, 5, 5]
