import pickle
def po_size(levels_list):
    count=0
    for x in range (len(levels_list)):
        for y in range (len(levels_list[x])):
            count = count + 1
    return count

def partialRec(largeList):
    if largeList[len(largeList)-1] == []:
        file_name=str(len(largeList[0][0])) + "_by_"+str(len(largeList[0][0][0]))

        with open('%s.txt' % file_name, "wb") as file:
            pickle.dump(largeList[:len(largeList)-1], file)

        return largeList[:len(largeList)-1]
    else:
        #list of matrices at this level
        levelList = largeList[len(largeList)-1]
        newLevel=[]
        flatten=[]
        for x in range (len(levelList)):
            newLevel.append(partialOrder(levelList[x]))
        for w in range (len(newLevel)):
            for o in range (len(newLevel[w])):
                if newLevel[w][o] not in flatten: #if we didn't already add matrix to flatten, add it
                    flatten.append(newLevel[w][o])
        largeList.append(flatten)
        return partialRec(largeList) #recursion

#Takes in a matrix and returns all of the iterations for the next level derived from that (all output matrices from one matrix)
def partialOrder(matrix):
    levelList=[]
    copy = matrix.copy()
    #columns - 1 because we don't need to look at the final column since there's nothing to the right


    for col in range (len(matrix[0])-1):
        for row in range (len(matrix)):
            current = matrix[row][col]

            for cols in range (col+1, len(matrix[0])):
                for rows in range (len(matrix)):

                    if (copy[rows][cols] == current + 1 and row != rows):

                        temp=current
                        copy[row][col]=copy[rows][cols]
                        copy[rows][cols]=temp
                        

                        copy2 = [[0] * len(matrix[0]) for i in range (len(matrix))]
                        for x in range (len(matrix)):
                            for y in range (len(matrix[0])):
                                copy2[x][y] = copy[x][y]
                                

                        levelList.append(copy2)

                        #resets copy
                        for x in range (len(matrix)):
                            for y in range (len(matrix[0])):
                                copy[x][y] = matrix[x][y]

                        if (current != matrix[row][col]):
                            break
                if (current != matrix[row][col]):
                    break

    return levelList
def compare(largeList, matrix1, matrix2):
    if matrix1 and matrix2 in largeList[len(largeList)-1]:
        print("Both tableaux are on the same level of the partial order.")
    elif matrix1 in largeList[len(largeList)-1]:
         print(str(matrix2) + " is higher in the partial order.")
         return None
    elif matrix2 in largeList[len(largeList)-1]:
        print(str(matrix1) + " is higher in the partial order.")
        return None
    elif largeList[len(largeList)-1] == []:
        print("Both tableaux inputs are incorrect.")
        
    else:
        #list of matrices at this level
        levelList = largeList[len(largeList)-1]
        newLevel=[]
        flatten=[]
        for x in range (len(levelList)):
            newLevel.append(partialOrder(levelList[x]))
        for w in range (len(newLevel)):
            for o in range (len(newLevel[w])):
                if newLevel[w][o] not in flatten: #if we didn't already add matrix to flatten, add it
                    flatten.append(newLevel[w][o])
        largeList.append(flatten)
        return compare(largeList, matrix1, matrix2) #recursion
    

# Improve efficiency by making the data structures a list of set of matrices, rather than a list of list of matrices
#Creates the matrix and calls partialRec
if __name__ == "__main__":
    print("")
    print("Welcome to tableaux partial order!\n")
    print("Enter compare to see which of two matrices is higher in the partial order")
    print("Enter data to add m x n tableaux partial order to database")
    print("Enter find to learn about a specific tableau in the database")
    print("Enter done to end the program\n")

    option=""
    while (option != "done"):
        print("")
        option = input("Select an option: ")
        option = option.strip()
        print("")
        if(option=="find"):

            rows = input("Rows of Tableau: ")
            columns = input("Columns of Tableau ")

            file_name=str(rows) + "_by_"+str(columns)
            try:

                with open('%s.txt' % file_name, "rb") as fp:   # Unpickling
                    matrix = pickle.load(fp)
            except:
                print("")
                print("This tableau is not in database")
                continue

            print("Enter print to print the partial order")
            print("Enter level to find/print a level of the partial order")
            #print("Enter lookup to find the location of a matrix in the partial order")
            print("Enter quantity to find the total number of m x n tableaux")
            print("Enter length to find the length of the partial order") #How many levels in partial order
            print("Enter done to end program\n")

            option=input("Select an option: ")
            option = option.strip()
            
            if (option == "level"):
                level = input("Select a level: ")
                print(matrix[int(level)-1])
            elif (option == "length"):
                print(len(matrix))
            elif (option == "quantity"):
                print(po_size(matrix))
            #elif (option=="lookup"):
                #print("Not yet implemented")
            elif (option=="print"):
                for x in range(len(matrix)):
                    print(matrix[x])
                    print("\n")
        elif (option =="compare"):
            SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
            numRow = int(input("Rows of Tableau: "))
            numCol = int(input("Columns of Tableau "))
            matrix1 = [[0]*numCol for i in range(numRow)]
            for i in range(numRow):
                for j in range(numCol):
                    matrix1[i][j] = int(input("Enter entry "+ "T"+str(i+1).translate(SUB)+str(j+1).translate(SUB)+": "))
            print ("Now, enter your second tableau.")
            matrix2 = [[0]*numCol for i in range(numRow)]
            for i in range(numRow):
                for j in range(numCol):
                    matrix2[i][j] = int(input("Enter entry "+ "T"+str(i+1).translate(SUB)+str(j+1).translate(SUB)+": "))
            standard_matrix = [[0] * numCol for i in range (numRow)]
            for j in range (numCol):
                for i in range (numRow):
                    standard_matrix[i][j] = j*numRow + i+1
            compare([[standard_matrix]], matrix1, matrix2)
                    
        elif (option =="data"):

            numRow = int(input("Enter the number of rows of the tableau "))
            numCol = int(input("Enter the number of columns of the tableau "))
            matrix = [[0] * numCol for i in range (numRow)]
            for j in range (numCol):
                for i in range (numRow):
                    matrix[i][j] = j*numRow + i+1

            list_mat = partialRec([[matrix]])

    print("Program has ended.")
