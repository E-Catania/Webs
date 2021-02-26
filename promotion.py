def promote(matrix):
    row,col = 0,0
    while (col < len(matrix[0])-1 or row < len(matrix)-1):
        if row == len(matrix)-1:
            matrix[row][col] = matrix[row][col+1]
            row,col = row,col+1
            continue
        if col == len(matrix[0])-1:
            matrix[row][col] = matrix[row+1][col]
            row,col = row+1,col
            continue

        if matrix[row+1][col] > matrix[row][col+1]:
            matrix[row][col] = matrix[row][col+1]
            row,col = row,col+1
        else:
            matrix[row][col] = matrix[row+1][col]
            row,col = row+1,col

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j]-1
    matrix[len(matrix)-1][len(matrix[0])-1]= len(matrix) * len(matrix[0])

    print(matrix)

def main():
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
   #Get an mxn tableau from user
    numRow = int(input("Please enter the number of rows of the tableau "))
    numCol = int(input("Please enter the number of columns of the tableau "))
    matrix=[[0]*numCol for i in range(numRow)]
    for i in range(numRow):
        for j in range(numCol):
            matrix[i][j] = int(input("Please enter entry "+ "T"+str(i+1).translate(SUB)+str(j+1).translate(SUB)+" "))
    promote(matrix)
main()





    
