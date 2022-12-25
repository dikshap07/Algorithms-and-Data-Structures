def spiralMatrix(matrix):
    m,n = len(matrix),len(matrix[0])
    print(f"m : {m} , n : {n}")
    left,right = 0,n-1

    up,down = 0, m-1
    res = []

    while len(res) < n*m:

        #traverse left
        
        for col in range(left,right+1):

            res.append(matrix[up][col])

        print(f"res after step 1  : {res} \n")

        #traverse down

        for row in range(up+1,down+1):
            
            res.append(matrix[row][right])

        print(f"res after step 2 : {res} \n")

        #making sure we are not on the same row

        if up != down:

            #traverse right to left

            for col in range(right-1,left-1,-1):

                res.append(matrix[down][col])
        
        print(f"res after step 3 : {res} \n")

        #making sure we are not on the same col
        
        if left != right:

            #traverse down to up

            for row in range(down-1,up,-1):
                # print("n-col_iter", n- col_iter)
                res.append(matrix[row][left])

        print(f"res after step 4  : {res} \n")


        left += 1
        right -=1
        up +=1
        down -=1



    return res


# print("Final Output : ",spiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))
# print("Final Output : ",spiralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
matrxi = [[1,2,3,5,6],[4,5,6,23,1],[7,8,9,3,2]]
# [[1,2,3],[4,5,6]]
print("Final Output : ",spiralMatrix(matrxi))


# [1,2,3,4,8,12,11,10,9,5,6,7]
[1,2,3,5,6,1,2,3,9,8,7,4,5,6,23]



