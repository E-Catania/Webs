def promote(matrix):
    #Blank space moves around, #'s below/right of space are compared until can't anymore
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

    return matrix

def main():
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
   #Get an mxn tableau from user
    numRow = int(input("Please enter the number of rows of the tableau "))
    numCol = int(input("Please enter the number of columns of the tableau "))
    matrix=[[0]*numCol for i in range(numRow)]
    for i in range(numRow):
        for j in range(numCol):
            matrix[i][j] = int(input("Please enter entry "+ "T"+str(i+1).translate(SUB)+str(j+1).translate(SUB)+" "))
    copy=[[0]*numCol for i in range(numRow)]
    for i in range(numRow):
        for j in range(numCol):
            copy[i][j] = matrix[i][j]
    print("The tableau you entered is "+str(copy)+".")
    print("The rest of the tableaux in the orbit:")
    count = 0
    # Prints the rest of the tableaux in the orbit
    for k in range(0, numRow * numCol):
        M = promote(copy)
        isDifferent = False
        for l in range(0, numCol):
            for n in range(0, numRow):
                if matrix[n][l] != M[n][l]:
                    isDifferent = True
            if isDifferent:
                break 
        if isDifferent:
            print(M)
            count+=1
        else:
            break
    print("The length of the orbit is "+str(count+1)+".")
        
main()





    
