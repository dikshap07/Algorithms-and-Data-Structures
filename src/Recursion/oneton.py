def oneton(n):


    if n == 0:
        return
    

    oneton(n-1)

    print(n)

# oneton(10)


def ntoone(n):

    if n == 0:
        return

    print(n)

    ntoone(n-1)

# ntoone(10)


def factorial(n):

    if n == 0:

        return 1

    return n * factorial(n-1)

print(factorial(4))

def sum_n(n):

    if n == 0:
        return 0

    return n + sum_n(n-1)

sum_n(5)


#sum of digits

def sum_digits(N):

    if N == 0:

        return N

    return sum_digits(N//10) + (N%10)

print(sum_digits(12))

#product of digits

def product_digits(N):

    if N %10== N:  #if one digit is remaining

        return N

    return product_digits(N//10) * (N%10)

print(product_digits(5555234))


#reverse a number

import math

def reverse(N):


    digits = int(math.log(N,10))
    print(digits)

    def helper(n,digits):

        if n%10 == n:
            return n

        return int(n%10)*(10**(digits)) + helper(n//10,digits-1)

    return helper(N,digits)

print(reverse(123456))


#return count of zeros in a number


def countZeros(N):

    def helper(N,count):

        if N == 0:
            return count
        
        rem = N%10
        if rem == 0:
            count+=1

            return helper(N//10,count)
    
        return helper(N//10,count)

    return helper(N,0)

print(countZeros(10100))
