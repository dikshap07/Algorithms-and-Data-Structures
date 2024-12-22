"""
In a matrix or a maze, give all paths but now you can go in all 4 directions, up down left right

"""

def allPaths(matrix,processed,row,col):

    if row == len(matrix)-1 and col == len(matrix[0])-1:
        print(processed)
        return


    if not matrix[row][col]: return

    #Up
    if row < len(matrix)-1:
        allPaths(matrix,processed + "U",row+1,col) #we are starting from (0,0) this time
    #right
    if col <len(matrix[0])-1:
        allPaths(matrix, processed + "R", row, col +1)
    #Down
    if row > 0:
        allPaths(matrix,processed + "D",row-1,col)
    #Left
    if col > 0:
        allPaths(matrix,processed + "D",row,col-1)

    return


def allPathsCorrect(matrix,processed,row,col):
    """
    We will mark all visited cells as False
    """

    if row == len(matrix)-1 and col == len(matrix[0])-1:
        print(processed)
        return


    if not matrix[row][col]: return

    matrix[row][col] = False
    #Up
    if row < len(matrix)-1:
        allPathsCorrect(matrix,processed + "D",row+1,col) #we are starting from (0,0) this time

    #right
    if col <len(matrix[0])-1:
        allPathsCorrect(matrix, processed + "R", row, col +1)

    #Down
    if row > 0:
        allPathsCorrect(matrix,processed + "U",row-1,col)

    #Left
    if col > 0:
        allPathsCorrect(matrix,processed + "L",row,col-1)

    matrix[row][col] =  True  #because now we are out of all the recursive calls for this cell,
                                # we need to restore its value
    return


def printPaths(matrix):

    paths = allPathsCorrect(matrix,"",0,0)
    print(matrix)
    return paths
"""
allPaths above is gonna give 'Stack overflow'.
allPathsCorrect fixes the problem
"""



if __name__ == "__main__":
    maze = [
        [True, True, True],
        [True, True, True],
        [True, True, True]
    ]

    print(printPaths(maze))