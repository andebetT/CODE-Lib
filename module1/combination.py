def nCr(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return  nCr(n - 1, r - 1)*n//r

# Test the function
n = 5
r = 3
result = nCr(n, r)
print(f"The value of {n}C{r} is {result}.")