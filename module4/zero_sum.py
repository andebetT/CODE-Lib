def zero_sum(numbers):
    subsets = [[]]  # Initialize with an empty subset
    result = []
    for num in numbers:
        new_subsets = []
        for subset in subsets:
            new_subset = subset + [num]
            if sum(new_subset) == 0 and 0 not in new_subset:
                result = new_subset
                break
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
    print(subsets)

    return result
numbers = [1, -2, 6, 7, 1]
number = [0, 0, 1, 3, 6, -4, -1]
print(zero_sum(numbers))
#print(zero_sum(number))