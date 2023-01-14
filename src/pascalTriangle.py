

def pascalTriangle(nrows):


    tri = []

    for row in range(nrows):

        row_i = [1 for i in range(row+1)]

        if row > 1:

            for j in range(1,row):

                row_i[j] = tri[row-1][j-1] + tri[row-1][j]

            print(f"{row_i : {row_i}}")

        
        tri.append(row_i)

    return tri

print(pascalTriangle(6))


# print([1 for i in range(1)])