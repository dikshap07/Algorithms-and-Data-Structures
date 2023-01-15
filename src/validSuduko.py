

board =  [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]




def validSudoku(board):


    row_has = [set() for i in range(9)]
    col_has = [set() for i in range(9)]
    box_has = [set() for i in range(9)]


    for row in range(9):

        for col in range(9):



            element = board[row][col]
            if element == ".":

                continue

            #check row 

            if element in row_has[row]:

                return False
            
            row_has[row].add(element)


            if element in col_has[col]:

                return False

            col_has[col].add(element)


            idx = (row//3)*3 + (col//3)

            if element in box_has[idx]:

                return False
            
            box_has[idx].add(element)

    return True


















# #TOO BRUTE FORCE, Checks every row and col individually


# def validSudoko(board):

#     #to check rule 1
#     row_hash = {}
    
#     for row in range(9):

#         for i in range(9):
#             if board[row][i]== ".":
#                 continue

#             elif (board[row][i],row) not in row_hash:

#                 row_hash[(board[row][i],row)] = 1

#             else :
#                 print(f"row_hash: {row_hash}")
#                 row_hash[(board[row][i],row)] += 1 
#                 # print(f"row_hash: {row_hash}")
#                 return False

#     print("rows all correct")

#     #to check Rule 2
#     col_hash = {}

#     for col in range(0,9):

#         for i in range(0,9):
#             if board[i][col]== ".":
    #             continue
    #         print(f"(board[{i}][{col}],{col}) = {(board[i][col],col)}")
    #         if (board[i][col],col) not in col_hash:

    #             col_hash[(board[i][col],col)] = 1

    #         else:

    #             col_hash[(board[i][col],col)] += 1 
    #             return False

    # print("columns all correct")


    # return True

print(validSudoko(board))


# if (board[i][col] in row_hash and row_hash[board[i][col]][2] == col) and row_hash[board[i][col]][1] != i:

#     print("repeated in row and col")
N = 9

rows = [set() for _ in range(N)]
print(2//3)