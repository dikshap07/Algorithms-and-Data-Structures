
from collections import deque


# def matrixReshape(mat,r,c):

#     m,n = len(mat),len(mat[0])

#     res = [[0 for i in range(c)] for j in range(r)]

#     row, col = 0,0

#     if m*n != r*c:

#         return mat


#     for i in range(m):

#         for j in range(n):

#             res[row][col] = mat[i][j]
#             col+=1

#             if col == c:

#                 row+=1
#                 col = 0

#     return res
 







#using mod and division

# def matrixReshape(mat,r,c):

#     m,n = len(mat),len(mat[0])

#     res = [[0 for i in range(c)] for j in range(r)]

#     count = 0

#     if m*n != r*c:

#         return mat

#     for i in range(m):

#         for j in range(n):

#             res[count//c][count%c] = mat[i][j]
#             count+=1
              

#     return res

# def matrixReshape( mat, r: int, c: int):
# 	m = len(mat)
# 	n = len(mat[0])
# 	if n*m!=r*c: #if the total number of elements in the original matrix wouldn't fit into a r by  c matrix
# 		return mat #return original
# 	ans = [[0 for i in range(c)] for j in range(r)] #new empty matrix
# 	num = 0 #keep track of how many elements we have added to our new array
# 	for i in range(m): #iterating through mat
# 		for j in range(n):
# 			row = num//c #the row we are writing into
# 			col = num%c #the column we are writing into
# 			ans[row][col] = mat[i][j] #add this element to the row in ans
# 			num+=1 #we added the last element
# 	return ans









def matrixReshape(mat, r: int, c: int):


    # check if legal

    m,n = len(mat),len(mat[0])
    queue = []

    if r*c != m*n:  #legal
        return mat

    res = [[0 for i in range(c)] for k in range(r)]

    for i in range(m):
        for j in range(n):

            queue.append(mat[i][j])

    for i in range(r):

        for j in range(c):

            res[i][j] = queue.pop(0)       
    return res


# def matrixReshape(mat, r: int, c: int):
#     m,n = len(mat),len(mat[0])
#     if r*c!=m*n:
#         return mat

#     res = [[0 for i in range(c)] for k in range(r)]
    
#     queue = []
#     for i in range(m):
#         for j in range(n):

#             queue.append(mat[i][j])

#     for i in range(r):

#         for j in range(c):

#             res[i][j] = queue.pop(0)  

#     return res

print(matrixReshape([[2,3],[4,5]],2,4))