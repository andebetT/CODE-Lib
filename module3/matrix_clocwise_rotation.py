def transpose_matrix_inplace(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(i ,cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(rows//2):
        for j in range(rows):
            matrix[j][i],matrix[j][rows-1-i]=matrix[j][rows-1-i],matrix[j][i]
    return matrix


# Example usage
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(transpose_matrix_inplace(matrix))
