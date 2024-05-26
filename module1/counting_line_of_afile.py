def count_lines_in_file(file_path):
    line_count = 0
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            line_count += 1
    return line_count