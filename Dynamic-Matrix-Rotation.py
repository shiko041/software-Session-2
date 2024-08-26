def rotate_matrix_90(matrix):
    num_rows = len(matrix)
    for i in range(0,num_rows):
        for j in range (i,num_rows):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(0,num_rows):
        for j in range(0,num_rows//2):
            matrix[i][j],matrix[i][num_rows-j-1]=matrix[i][num_rows-j-1],matrix[i][j]
def rotate_matrix(matrix,degree):
    if degree %90 ==0 and degree>0:
        rotate_matrix(matrix,degree-90)
        rotate_matrix_90(matrix)
        
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate 90 degrees clockwise
rotate_matrix(matrix,360)
print(matrix)