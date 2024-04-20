def adddition_of_matrix(rows,col,matrix1,matrix2): #defnetion for adddition of matrix two matrix function
    added_matrix = []  
    # iterate through lists
    for i in range(rows):   
        each_row = []
        for j in range(col):
            each_row.append(matrix1[i][j] + matrix2[i][j])  #adding the each elements from both matrix
        added_matrix.append(each_row)
        each_row = []
    return added_matrix

rows = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
matrix1 = []
#this is used to read the matrix according to number of rows
for i in range(rows):
    matrix1.append(list(map(int,input().split())))
#but hear we considering the matrix(A) == matrix(B)
matrix2 = matrix1
#calling the function
added_matrix = adddition_of_matrix(rows,col,matrix1,matrix2)
print(added_matrix)