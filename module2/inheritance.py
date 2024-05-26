class Human:
    def __init__(self,name):
        self.name=name
    def work(self):
        print("human is worker")
    def speak(self):
        print("human can speak")
class Boy(Human):
    def inheritance(self):
        print("this called single inheritance")
class Andebet(Boy):
    def iheritance_type(self):
        print("this multilevel inheritance")
class Astu:
    pass
class Epce:
    pass
class Adama(Astu,Epce):
    def multiple_inheritance(self):
        print("this is multiple inheritance")



set1={1,2,3}
set2={3,4,5}
print(set1-set2)