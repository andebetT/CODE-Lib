def calculate_sums(list1):
    result = []
    next_larger = []

    # Find the next larger integer for each element in the list
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[j] > list1[i]:
                next_larger.append(list1[j])
                break
        else:
            next_larger.append(None)

    # Calculate the sums and append to the result list
    for i in range(len(list1)):
        if next_larger[i] is not None:
            result.append(list1[i] + next_larger[i])
        else:
            result.append(list1[i])

    return result
list1=[4,6,7,3,9,5,4,1,8,3,2]
print(calculate_sums(list1))
