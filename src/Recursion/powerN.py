
"""
Write function to get x to the power n.
"""

def power(x,n):
    #binomial exponential

    if n == 0: return 1
    if n <0:
        return (1/power(x,-n))

    if n%2 != 0: #odd

        return (x)*power(x*x,(n-1)//2)

    else:
        return power(x*x,n//2)


print(power(16,2))
