"""
In the allPathsCorrect problem, also print the path/matrix for each path
i.e. : 0,None,None  :This is a path - DDRR
       2,None,None
       3,4   ,5
"""


def allPathsMatrix(matrix,processed,row,col,level):

    if row == len(matrix)-1 and col == len(matrix[0])-1:
        matrix[row][col] = level
        print(processed)
        for row in matrix:
            print(f"{row}")
        print("-----------------")
        return


    if matrix[row][col] != 0: return

    matrix[row][col] = level

    if row < len(matrix)-1:
        allPathsMatrix(matrix,processed + "D",row+1,col,level+1) #we are starting from (0,0) this time
    #right
    if col <len(matrix[0])-1:
        allPathsMatrix(matrix, processed + "R", row, col +1,level+1)
    #Down
    if row > 0:
        allPathsMatrix(matrix,processed + "U",row-1,col,level+1)
    #Left
    if col > 0:
        allPathsMatrix(matrix,processed + "L",row,col-1,level+1)

    matrix[row][col] = 0


    return


def printPaths(matrix):
    # path = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    paths = allPathsMatrix(matrix,"",0,0,1)
    # print(matrix)
    return paths

if __name__ == "__main__":
    maze = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    print(printPaths(maze))