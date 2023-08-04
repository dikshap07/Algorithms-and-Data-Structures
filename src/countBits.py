"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

"""


def countOnes(n):

    ones = 0

    while n:

        n = n & (n-1)
        ones+=1

    return ones



def countBits(n):

    res = []

    for i in range(n+1):
        res.append(countOnes(i))

    return res



if __name__ == "__main__":

    print(countBits(7))
    print(countBits(2))