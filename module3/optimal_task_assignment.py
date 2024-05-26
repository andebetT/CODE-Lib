def optimal_Task_Assignment(array):
    array.sort()
    list1 = []
    for i in range(len(array) // 2):
        list1.append((array[i], array[~i]))
    return sum(list1[-1])


a = [6, 3, 2, 7, 5, 5]
print(optimal_Task_Assignment(a))

