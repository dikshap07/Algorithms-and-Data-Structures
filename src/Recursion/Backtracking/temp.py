"""
In the allPathsCorrect problem, also print the path/matrix for each path
i.e. : 1,None,None  :This is a path - DDRR
       2,None,None
       3,4   ,5
"""


def allPathsMatrix(matrix,processed,row,col,level,path):

    if row == len(matrix)-1 and col == len(matrix[0])-1:
        path[row][col] = level
        print(processed)
        print(path)
        print("-----------------")
        return


    if not matrix[row][col]: return

    matrix[row][col] = False

    path[row][col] = level

    if row < len(matrix)-1:
        allPathsMatrix(matrix,processed + "D",row+1,col,level+1,path) #we are starting from (0,0) this time
    #right
    if col <len(matrix[0])-1:
        allPathsMatrix(matrix, processed + "R", row, col +1,level+1,path)
    #Down
    if row > 0:
        allPathsMatrix(matrix,processed + "U",row-1,col,level+1,path)
    #Left
    if col > 0:
        allPathsMatrix(matrix,processed + "L",row,col-1,level+1,path)

    matrix[row][col] = True


    return


def printPaths(matrix):
    path = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    paths = allPathsMatrix(matrix,"",0,0,1,path)
    # print(matrix)
    return paths

if __name__ == "__main__":
    maze = [
        [True, True, True],
        [True, True, True],
        [True, True, True]
    ]

    print(printPaths(maze))