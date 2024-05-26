class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def grt_items(self):
        return self.items
    def is_impety(self):
        return self.items==[]
    def top_ofstack(self):
        if not self.items:
            return self.items[-1]
s=Stack()
list1=[1,2,3,4]
for i in list1:
    s.push(i)
print(s.grt_items())
print(s.is_impety())

#usestack to implement weather a string have balanced paranthesis
def is_valid(string):
    d={"{":"}","[":"]","(":")"}
    stack=[]
    for i in string:
        if i in d:
            stack.append(i)
        elif not stack or d[stack.pop()]!=i:
            return False
    return len(stack)==0
print(is_valid("{}[]"))


#converting decimal to binary using stack
def convert_to_binary(decimal):
    stack=[]
    while decimal>0:
        reminder=decimal%2
        stack.append(reminder)
        decimal=decimal//2
    bin_val=""
    while not stack:
        bin_val+=stack.pop()
    return bin_val
print(convert_to_binary(234))
