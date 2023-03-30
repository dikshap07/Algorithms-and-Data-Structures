
def pacificAtlantic(heights):

    #if matrix is empty return empty list
    if not heights or not heights[0]:  #i.e. either matrix empty == [] or if first row is empty == [[]]

        return []


    #initialize variables to store num of rows,columns and to store cells - sets

    total_rows,total_columns = len(heights),len(heights[0])
    pacific_reachable_cells = set()  #because we dont want to repeat cells
    atlantic_reachable_cells = set()  


    #dfs

    def dfs(r,c,reachable): #reachable : set containing visited cell

        reachable.add((r,c))

        #movement in 4 directions (-1,0) = north , (0,+1) = east, (+1,0) = south , (0,-1) = west 

        for row_dir,col_dir in [(-1,0),(0,1),(1,0),(0,-1)]:

            new_row = r + row_dir
            new_col = c + col_dir

            #check if the direction in movement is not valid:

            if new_row < 0 or new_col < 0 or new_row >= total_rows or new_col >= total_columns:
                continue #no dfs if not valid move to next neighbour

            #check if new cell is already in reachable, move to next neighbour

            if (new_row,new_col) in reachable:
                continue

            #check if the height of the new cell is greater than main cell, if smaller move to next neighbour i.e continue

            if heights[new_row][new_col] < heights[r][c]:
                continue

            #now we can perform dfs on the new cell

            dfs(new_row,new_col,reachable)


    
    #traverses row-wise -> cells near oceans
    for i in range(total_rows):

        dfs(i,0,pacific_reachable_cells) 
        dfs(i,total_columns-1,atlantic_reachable_cells)                         

    #traverses column-wise -> cells near oceans

    for i in range(total_columns):

        dfs(0,i,pacific_reachable_cells) 
        dfs(total_rows-1,i,atlantic_reachable_cells) 


    return list(pacific_reachable_cells.intersection(atlantic_reachable_cells))



if __name__ == "__main__":

    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(pacificAtlantic(heights))