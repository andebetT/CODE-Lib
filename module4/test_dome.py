
class TextInput:
    def __init__(self):
        self.value = ""
    def add(self, character):
        self.value += character
    def get_value(self):
        return self.value
class NumericInput(TextInput):
    def add(self, character):
        if character.isdigit():
            self.value += character
input = NumericInput()
input.add("1")
input.add("a")
input.add("0")
print(input.get_value())



dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
list1 = ["a", "b", "c"]

# Create a new dictionary with filtered elements
filtered_dict = {key: value for key, value in dictionary.items() if key in list1}

print(filtered_dict)

dictionary ={"a":1,"b":2,"c":3,"d":4,"e":5}
list1=["a","b","c"]
