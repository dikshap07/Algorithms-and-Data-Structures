
def maxAreaOfIsland(grid):

    R,C = len(grid),len(grid[0])


    if not grid: return 0

    area = 0

    def dfs(i,j):
        count = 0
        if i < 0 or j < 0 or i>= R or j >= C or grid[i][j] != 1:  #dont perform dfs
            return count

        count = 1
        grid[i][j] = "#"   #marks node as visited so that element is not counted twice

        count += dfs(i+1,j)  
        count += dfs(i,j+1)
        count += dfs(i-1,j)
        count += dfs(i,j-1)
    
        return count

    for i in range(R):
        for j in range(C):

            if grid[i][j] == 1:
                
                area = max(area,dfs(i,j))
    
    return area


if __name__ == "__main__":

    grid = [[1]]
    # [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

    print(maxAreaOfIsland(grid))