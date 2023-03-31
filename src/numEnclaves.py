

def numEnclaves(grid) :

    if not grid or not grid[0]:
        return 0

    boundary_reachable = set()
    boundary_not_reachable = set()
    R,C = len(grid),len(grid[0])


    def dfs(r,c,reachable):
        # print(f"r,c = {r,c}")

        reachable.add((r,c))

        for x,y in [(1,0),(0,1),(0,-1),(-1,0)]:

            new_r = r +x
            new_c = c+y
            
            #if invalid cell
            if new_r < 0 or new_c < 0 or new_r >= R or new_c>= C or grid[r][c] != 1:

                continue


            #if already reached

            if (new_r,new_c) in reachable:
                continue

            dfs(new_r,new_c,reachable)

    

    #0th row traversal
    for i in range(len(grid[0])):

        if grid[0][i] == 1:
            dfs(0,i,boundary_reachable)

    #for 0th column traversal
    for i in range(1,len(grid)): #can skip grid[0][0] coz already visited

        if grid[i][0] == 1:
            dfs(i,0,boundary_reachable)

    #for (C-1)th column traversal
    for i in range(1,len(grid)): #can skip grid[0][C-1] coz already visited

        if grid[i][C-1] == 1:
            dfs(i,C-1,boundary_reachable)

    #R-1 th row traversal
    for i in range(1,len(grid[0])-1): #can skip grid[R-1][0] and grid[R-1][C-1] coz already viisted

        if grid[R-1][i] == 1:
            dfs(R-1,i,boundary_reachable)

    
    # print(boundary_reachable)
    for i in range(R):
        for j in range(C):

            if (i,j) not in boundary_reachable and grid[i][j] == 1:

                boundary_not_reachable.add((i,j))
    
    # print(boundary_not_reachable)

    return len(boundary_not_reachable)


if __name__ == "__main__":

    # grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    # print(numEnclaves(grid))

    assert(numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]) == 0)
    assert(numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])==3)