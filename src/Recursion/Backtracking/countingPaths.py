"""
Count the number of paths btw 2 points in a 2D matrix, where you can only either go right or down
Here, start with top left most corner to bottom right most corner i.e. (n,n) to (0,0)
"""

def pathsUntil(row,col):

    if row == 0 or col ==0: return 1 #last row or col only 1 possible path to point

    paths_down = pathsUntil(row-1,col)
    paths_right = pathsUntil(row,col-1)

    return paths_down + paths_right


def countPaths(n):

    paths = pathsUntil(n-1,n-1)

    return paths


#Note: we can just save the num of paths unitl a point in a hashmap, and solve this using dynamic programming

if __name__ == "__main__":

    n = 3
    print(countPaths(5))