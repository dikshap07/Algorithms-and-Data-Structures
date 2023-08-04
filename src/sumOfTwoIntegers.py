"""Given two integers a and b, return the sum of the two integers without using the operators + and -"""


def getSum(m, n):

    x, y = abs(m),abs(n)
    #making sure m> n:
    if x< y :

        return getSum(n,m)

    #store the sign
    sign = 1 if m> 0 else -1

    #if both same sign
    if m*n >=0 :
        #problem : sum of two positive ints

        while y:
            x,y = (x^y),(x&y)<<1

    #if both opp signs
    else: 
        #problem : substract two positive ints
        while y:
            x,y = (x^y),((~x)& y)<<1

    return sign*x


def xor(a, b):
    print(f"a = {bin(a)[2:]}")
    print(f"b = {bin(b)[2:]}")

    print(f"xor of a,b : {a^b}")
    return a^b


if __name__ == "__main__":
    print(getSum(5, -17))

    # print(bin(xor(2, 4))[2:])
