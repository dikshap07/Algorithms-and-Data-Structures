def printStar(n):

    print(("* ")*n)

    if n-1 == 0: return

    return printStar(n-1)


printStar(6)
print("--------------------------------")


def upsidedownTriangle(row,col):

    if row == 0: return

    if col < row:
        print("* ", end="") #this ensures that the end is not a new line - which is the default

        upsidedownTriangle(row,col+1)

    else:
        print("") #this ensures that now we move to a new line instead of just the next space
        upsidedownTriangle(row-1,0)

upsidedownTriangle(6,0)

print("------------------------")

def triangle(row,col,n):

    if row == n+1: return

    if col< row:
        print("* ",end = "")
        triangle(row,col+1,4)
    else:
        print("")

        triangle(row+1,0,4)

triangle(0,0,4)
print("---------")

def triangle2(row,col):

    if row == 0: return

    if col< row:
        triangle2(row,col+1)


    else:
        triangle2(row-1,0)
        print(" ")

triangle2(4,0)