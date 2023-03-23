def floodFill(image,sr,sc,color):

    source_color = image[sr][sc]
    new_color = color

    R,C = len(image),len(image[0])

    #if source node has the target color  image

    if source_color == new_color:  image

    #else perform dfs on all neighbouring nodes and source node

    def dfs(r,c):

        #if current node has source_color
        if image[r][c] == source_color: 
            
            #change its color to target
            image[r][c] = new_color

            #dfs on neighbour above
            if r>= 1:  dfs(r-1,c)

            #dfs on left neighbour
            if c>=1:  dfs(r,c-1)

            #dfs on neighbour below
            if r+1< R:  dfs(r+1,c)

            #dfs on right nrighbour
            if c+1 < C:  dfs(r,c+1)

    dfs(sr,sc)
    return image 


if __name__ == '__main__':

    # image=[[1,1,1],[1,1,0],[1,0,1]]
    image = [[0,0,0],[0,0,0]]
    sr=0
    sc =1
    color = 1 

    print(floodFill(image,sr,sc,color))