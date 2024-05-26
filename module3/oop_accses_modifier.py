'''class Attributes:
    def __init__(self):
        self.public="public attributes"
        self._protected="protected attributes"
        self.__private="private attributes"
obj=Attributes()
print(obj.public)
print(obj._protected)
print(obj._Attributes__private)#magling'''


class University:
    def __init__(self,gpa):
        self.gpa=gpa
        self.name="andebet"
        self.age=26
    def learn_students(self):
        print("learn students")
    def accept_students(self):
        print("accept students")
class School(University):
    def __init__(self,y,x):
        self.y=y
        self.department="EPCE"
        super().__init__(x)

    def learn_students(self):

        super().learn_students()
        print("i,m students")
school=School(34,6)
print(school.learn_students())
print(school.accept_students())
print(school.age)
print(school.name)
print(school.department)
print(school.gpa)
print(school.y)

