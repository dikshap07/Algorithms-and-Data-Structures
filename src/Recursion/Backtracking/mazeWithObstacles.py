"""
print the paths btw 2 points in a 2D matrix/maze, where you can only either go right or down
Here, start with top left most corner to bottom right most corner i.e. (n,n) to (0,0)
And it has obstacles.



Maybe we will be given a boolean matrix where False means obstacle.
"""

def pathsUntil(matrix,processed,row,col):

    if row == 0 and col ==0:

        print(processed)
        return  #last row or col only 1 possible path to point
#we can also just add the condition to check if a matrix index is set of False return Nothing there if it is keeping other
    #things same i.e no " and matrix[row-1][col]==1 " required
    if row >0 and matrix[row-1][col]==1:
        pathsUntil(matrix,processed + "D",row-1,col)
    if col >0 and matrix[row][col-1]==1:
        pathsUntil(matrix,processed + "R",row,col-1)


    return

def pathsUntilList(processed,row,col):
    path = []
    if row == 0 and col ==0:

        print(processed)

        return [processed]#last row or col only 1 possible path to point


    if row >0:
        path.extend(pathsUntilList(processed + "D",row-1,col))
    if col >0:
        path.extend(pathsUntilList(processed + "R",row,col-1))
    if col>0 and row>0:
        path.extend(pathsUntilList(processed+"Di",row-1,col-1))

    return path

def printPaths(matrix,n):

    paths = pathsUntil(matrix,"",n-1,n-1)

    return paths


#Note: we can just save the num of paths unitl a point in a hashmap, and solve this using dynamic programming

if __name__ == "__main__":
    maze = [
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ]

    print(printPaths(maze,3))