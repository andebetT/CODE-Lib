def pascal_triangle(n):
    first_row = [1]
    rows = [first_row]
    for j in range(1, n):
        row = [1]
        for i in range(1, len(rows[-1])):
            num = rows[-1][i - 1] + rows[-1][i]
            row.append(num)
        row.append(1)
        rows.append(row)
    return rows
print(pascal_triangle(5))




def pask(n):
    rows=[[1]]
    for i in range(1,n):
        row=[1]
        for j in range(1,len(rows[-1])):
            num=rows[-1][i-1]+rows[-1][i]
            row.append(num)
        row.append(1)
        rows.append(row)


