"""
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].
"""

import math

def factorCombinations(N):

    res = []

    def getFactors_(n,factors,start):

        if factors:
            res.append(factors + [n]) #if factors is non empty, then add n to the list

        #else we iterate to find factors of current n, after already adding n to the factors list

        for num in range(start,math.sqrt(n)+1): #we only need to check until sqrt of current

            getFactors(n//num,factors + [num],num) #now update the num to n//num,
                                                    #add this num to our factors list
                                                    #start index changes to avoid duplicates

    getFactors_(N,[],2)

    return res

#Works but TLE
def getFactors(self, n: int):
    if n == 1:
        return []

    results = []
    def getCombs(processed,start,product):

        # product = 1
        # for i in processed:
        #     product= product*i

        if product == n:
            results.append(processed[:])
            return

        for num in range(start,n//2 + 1):

            # if len(processed)>1 and processed[-1]*num > n:
            #     break
            if product * num > n:
                break
            if n % num == 0:
                processed.append(num)
                # if processed[-1]*num <= n:
                getCombs(processed,num,product * num)

                processed.pop()

        # if product != n and product * n // product == n:
        #     results.append(processed + [n // product])
    getCombs([],2,1)


    return results
