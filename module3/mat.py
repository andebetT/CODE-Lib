def matricx_add(mat1,mat2):
    if len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0]):
        return None
    result=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]+mat2[i][j])
        result.append(row)
    return result
print(matricx_add([[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]))


#matrix multiplication
def matrix_multiplication(matrix1,matrix2):
    row1=len(matrix1)
    col1=len(matrix1[0])
    row2=len(matrix2)
    col2=len(matrix2[0])
    if col1!=row2:
        return None
    result=[[0 for _ in range(col2)] for _ in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]
print(matrix_multiplication(matrix1,matrix2))


def transpose_matrix(matrix):
    temp=[[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            temp[i][j]=matrix[j][i]
    return temp
print(transpose_matrix([[1,2,3],[4,5,6]]))


def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter the element at position ({i}, {j}): "))
            row.append(value)
        matrix.append(row)
    return matrix

# Get the dimensions of the matrix from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print(create_matrix(rows,cols))


def matrix_rotation(matrix,r):
    mat=[]
    m=len(matrix)
    n=len(matrix[0])
    k=min(m,n)//2
    for i in range(k):
        row=[]
        for j in range(i,n-1-i):
            row.append(matrix[i][j])
        for j in range(i,m-1-i):
            row.append(matrix[i][n-1-i])
        for j in range(n-1-i,i,-1):
            row.append(matrix[n-1-i][j])
        for j in range(m-1-i,i,-1):
            row.append(matrix[i][j])
        mat.append(row)
    for i in range(k):
        row=mat[i]
        idx=r%len(row)
        def increment():
            return (idx+1)%len(row)
        for j in range(i,n-1-i):
            matrix[i][j]=row[idx]
            idx=increment()
        for j in range(i,m-1-i):
            matrix[i][n-1-i]=row[idx]
            idx = increment()
        for j in range(n-1-i,i,-1):
            matrix[n-1-i][j]=row[idx]
            idx = increment()
        for j in range(m-1-i,i,-1):
            matrix[i][j]=row[idx]
            idx = increment()


    for i in matrix:
        print(*i)

