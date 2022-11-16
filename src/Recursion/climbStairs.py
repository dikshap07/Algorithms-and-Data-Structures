def climbStairs(n):   #recursion with memoisation


    uniques = {}

    def helper(n,uniques):
    
        if n == 1:
            uniques[n] = 1

        elif n == 2:
            uniques[n] = 2

        else:

            if n in uniques:
                return uniques[n]

            else:

                uniques[n] = helper(n-1,uniques) + helper(n-2,uniques)
        return uniques[n]
    return helper(n,uniques)





#DYNAMIC PROGRAMMING SOLUTION

def climbStairs_dp(n):

    num_ways = [0]*(n+1)

    num_ways[0] = 1  
    # so that when we do n-1 + n-2 for n ==2 we get 2 which is the number of ways to reach the step 2
    num_ways[1] = 1 

    for i in range(2,n+1):
        
        num_ways[i] = num_ways[i-1] + num_ways[i-2]
        
    return num_ways[n]


    memo = [0]*(n)


    return climb_stairs(0,n,memo)



def climbStairs(n):   #recursion
    
    if n == 1:
        return 1

    elif n == 2:
        return 2

    else:
        return climbStairs(n-2) + climbStairs(n-1)


print(climbStairs(38))
