def prevSmaller(A):
    stack = []
    result = []
    for i in range(len(A)):
        while stack and stack[-1] >= A[i]:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(A[i])
    return result
a=[4,5,2,10,8]
print(prevSmaller(a))