
from collections import deque

"""Without using extra space"""

def matrixReshape(mat,r,c):

    m,n = len(mat),len(mat[0])

    res = [[0 for i in range(c)] for j in range(r)]

    row, col = 0,0

    if m*n != r*c:

        return mat


    for i in range(m):

        for j in range(n):

            res[row][col] = mat[i][j]
            col+=1

            if col == c:

                row+=1
                col = 0

    return res
 







"""using mod and division"""

def matrixReshape(mat,r,c):

    m,n = len(mat),len(mat[0])

    res = [[0 for i in range(c)] for j in range(r)]

    count = 0

    if m*n != r*c:

        return mat

    for i in range(m):

        for j in range(n):

            res[count//c][count%c] = mat[i][j]
            count+=1
              

    return res


"""Using Queue"""



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



print(matrixReshape([[2,3],[4,5]],2,4))