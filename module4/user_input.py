# Initialize an empty list
my_list = []

# Read the input lines
input_lines = '''3
2
4
5
6'''

# Split the input into lines
lines = input_lines.split('\n')

# Extract the test case from the first line
test_case = int(lines[0])

# Iterate over the remaining lines and convert them to integers
for line in lines[1:]:
    element = int(line)
    my_list.append(element)

# Print the list
print(my_list)
Output:[2, 4, 5, 6]