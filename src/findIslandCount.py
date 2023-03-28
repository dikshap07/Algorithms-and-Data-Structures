def numIslands(grid):

    if not grid:  #if grid is empty return 0
        return 0

    R = len(grid)
    C = len(grid[0])

    islands = 0

    def dfs(i,j):

        if i < 0 or j < 0 or i>= R or j+1 >= C or grid[i][j] != "1":  #dont perform dfs
            return 

        grid[i][j] = "#"
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i,j-1)


    #traverse thru all the elements to find islands, count num of dfs called, bcoz dfs only called if element == 1

    for i in range(R):
        for j in range(C):

            if grid[i][j] == "1":

                dfs(i,j)

                islands+=1

    return islands


if __name__ == "__main__":

    grid = grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]


    print(numIslands(grid))