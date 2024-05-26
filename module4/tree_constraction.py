def TreeConstructor(strArr):
    # Create a dictionary to store the parent-child relationships
    parents = {}

    # Iterate through the input array
    for pair in strArr:
        # Extract the child and parent nodes from the pair
        child, parent = map(int, pair[1:-1].split(','))

        # If the child already has a parent, return False
        if child in parents and parents[child] != parent:
            return "false"

        # If the parent has more than 2 children, return False
        if parent in parents and len(parents[parent]) == 2:
            return "false"

        # Add the child-parent relationship to the dictionary
        if parent not in parents:
            parents[parent] = []
        parents[parent].append(child)

    # If we made it through the entire array without returning False, return True
    return "true"
list1=["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
list2= ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
list3=["(1,2)", "(2,4)", "(7,2)"]
print(TreeConstructor(list1))
print(TreeConstructor(list2))
print(TreeConstructor(list3))
