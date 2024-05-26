
#method1:brutforce solution
def set_matrix_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    # Find the rows and columns containing zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set the rows to zeros
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0

    # Set the columns to zeros
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0

# Example usage
matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
set_matrix_zeros(matrix)
#print(matrix)


def set_matrix_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Step 1: Find the zeros and mark the rows and columns
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                # Mark the row as -1
                for k in range(cols):
                    if matrix[i][k] != 0:
                        matrix[i][k] = -1
                # Mark the column as -1
                for k in range(rows):
                    if matrix[k][j] != 0:
                        matrix[k][j] = -1

    # Step 2: Change -1 elements to 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -1:
                matrix[i][j] = 0


# Example usage
matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
set_matrix_zeros(matrix)
#print(matrix)


#optimized_method
def set_matrix_zero(matrix):
    first_row=False
    first_col=False
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                if i==0:
                    first_row=True
                if j==0:
                    first_col=True
                matrix[i][0]=0
                matrix[0][j]=0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    if first_row:
        for i in range(m):
            matrix[0][i]=0
    if first_col:
        for i in range(n):
            matrix[i][0] = 0
    return matrix
matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
set_matrix_zeros(matrix)
print(matrix)



