#using dynamic programmming
def candy( A):
    n = len(A)
    candies = [1] * n
    for i in range(1, n):
        if A[i] > A[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if A[i] > A[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    min_candies = sum(candies)
    return min_candies
print(candy([1,5,3,2]))

def lis(A):
    pointer1 = 0
    maximum = 0
    if len(A) == 1:
        return 1
    for i in range(1, len(A)):
        if A[i] < A[i - 1]:
            pointer1 = i
        maximum = max(maximum, i - pointer1 + 1)
    return maximum
print(lis([89,69,54,19,51,16,54,64,89,72,40,31,43,1,11,82,65,75,67,25,98,31,77,55,88,85,76,35,101,44,74,29,94,72,39,20,24,23,66,16,95,5,17,54,89,93,10,7,88,68,10,11,22,25,50,18,59,79,87,7,49,26,96,27,19,67,35,50,10,6,48,38,28,66,94,60,27,76,4,43,66,14,8,78,72,21,56,34,90,89]))
