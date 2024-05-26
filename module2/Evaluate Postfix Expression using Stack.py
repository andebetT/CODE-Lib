def postfix_evaluato(array):
    oprator=["+","-","/","%","*"]
    stack=[]
    for i in array:
        if i not in oprator:
            stack.append(i)
        else:
            first=stack.pop()
            second=stack.pop()
            if i=="+":
                stack.append((int(first)+int(second)))
            if i=="-":
                stack.append((int(first)-int(second)))
            if i=="*":
                stack.append((int(first)*int(second)))
            if i=="/":
                stack.append((int(first)/int(second)))
            if i=="%":
                stack.append((int(first)%int(second)))
    return stack[-1]
array=["2","3","+","3","*"]
print(postfix_evaluato(array))


