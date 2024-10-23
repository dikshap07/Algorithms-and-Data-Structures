"""
print the paths btw 2 points in a 2D matrix/maze, where you can only either go right or down
Here, start with top left most corner to bottom right most corner i.e. (n,n) to (0,0)
"""

def pathsUntil(processed,row,col):

    if row == 0 and col ==0:

        print(processed)
        return  #last row or col only 1 possible path to point
    if row >0:
        pathsUntil(processed + "D",row-1,col)
    if col >0:
        pathsUntil(processed + "R",row,col-1)

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

    return path

def printPaths(n):

    paths = pathsUntilList("",n-1,n-1)

    return paths


#Note: we can just save the num of paths unitl a point in a hashmap, and solve this using dynamic programming

if __name__ == "__main__":

    n = 3
    print(printPaths(3))