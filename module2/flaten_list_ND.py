def flatten_array(array):
    flattened = []
    for element in array:
        if isinstance(element, list):
            flattened.extend(flatten_array(element))
        else:
            flattened.append(element)
    return flattened
array = [1, [2, 3], [4, [5, 6]], 7]
print(flatten_array(array))


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    #def displayEmployee(self):

em=Employee("andebet",20)
em=Employee("aastu",21)
em.displayCount()

a=[1,2,3,4,5]
a.insert(2,20)
print(a)

