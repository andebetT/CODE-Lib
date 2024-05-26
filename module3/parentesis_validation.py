def parenthesis_validation(A):
    stack = []
    dictionary = {"[": "]", "(": ")", "{": "}"}
    for i in A:
        if i in dictionary:
            stack.append(i)
        elif len(stack) == 0 or dictionary[stack.pop()] != i:
            return 0
    return 1 if len(stack) == 0 else 0
a="[][][()()({}{}"
print(parenthesis_validation(a))
