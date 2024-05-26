def add_matrices(mat1, mat2):
    # Check if the matrices have the same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions for addition"

    # Initialize an empty result matrix with the same dimensions
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result
# Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# Call the add_matrices function
result_matrix = add_matrices(matrix1, matrix2)
print(result_matrix)
# Function to multiply two matrices
def multiply_matrices(mat1, mat2):
    # Determine the dimensions of the input matrices
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])
   # Check if multiplication is possible
    if cols1 != rows2:
        return ("Matrix multiplication is not possible. Number of column")
    # Initialize the result matrix with zeros)
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
# Example matrices
matrix1 = [[1, 2, 3],
 [4, 5, 6]]
matrix2 = [[7, 8],
 [9, 10],
 [11, 12]]
# Multiply the matrices
result_matrix_mul = multiply_matrices(matrix1, matrix2)
print(result_matrix_mul)
# Function to transpose a matrix
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    # Create an empty matrix to store the transposed data
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    print(result)
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result
# Input matrix
matrix = [
 [1, 2, 3],
 [4, 5, 6]
]
# Transpose the matrix
transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)
#python program for quize using dictionary
q1='''python is a high level laungauge
a,TRUE
b,False '''
q2='''python was crated by ?
a,gudio,van
b,newton'''
qustion={q1:"a",q2:"b"}
score=0
for i in qustion:
    print(i)
    ans=input("please enter the ansewr")
    if ans==qustion[i]:
        print("you have got the ansewer")
        score+=1
    else:
        print("you didnot get the ansew")
print(score)

def mat_diag(matrix):
    sum1=0
    sum2=0
    for i in range(len(matrix)):
        sum1+=matrix[i][i]
        sum2+=matrix[i][len(matrix)-1-i]
    return abs(sum2-sum1)
mat=[[1,2,3],[4,5,6],[9,8,9]]
#print(mat_diag(mat))
def arry_even_odd(array):
    if len(array)==0:
        return  []
    first=[array[0]]
    for i in array[1:]:
        if i%2!=first[-1]%2:
            first.append(i)
    return  first
arr=[1,3,2,4,7,8,5]
#print(arry_even_odd(arr))
#this program is used to find the product of the array except it self
def product(nums):
    left_product=[]
    for i in range(0,len(nums)):
        if i==0:
            left_product.append(nums[i])
        else:
            left_product.append(left_product[-1]*nums[i])
    print(left_product)

    right_product=[]
    for i in range(len(nums)-1,-1,-1):
        if i==len(nums)-1:
            right_product.append(nums[i])
        else:
            right_product.append(right_product[-1]*nums[i])

    print(right_product)
    right_product=right_product[::-1]
    result=[]
    for i in range(len(nums)):
        if i==0:
            result.append(right_product[i+1])
        elif i==len(nums)-1:
            result.append(left_product[i-1])
        else:
            result.append(left_product[i-1]*right_product[i+1])
    return result
nums=[2,5,3,4]
print(product(nums))


