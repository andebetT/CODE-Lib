def function(f):
    if isinstance(f, str):
        return f[::-1]
    else:
        return f[1] ** f[0]
print(function(2,5))