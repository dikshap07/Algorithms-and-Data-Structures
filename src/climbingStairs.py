
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

# O(n) time O(1) space

def climbStairs( n: int) -> int:

    if n ==1 or n ==2:
        return n

    combinations = [1,2]

    i = 3
    while i < n:

        new_combo = combinations[0] + combinations[1]
        combinations[0],combinations[1] = combinations[1],new_combo

        print(f"combinations for i = {i}: {combinations}")
        i+=1

    return sum(combinations)


#O(n) time O(n) space

def climbStairsNN( n: int) -> int:
    combinations = {}
    combinations[1], combinations[2] = 1,2

    if n == 1 or n== 2:
        return n

    i = 3
    while i < n:

        if i not in combinations.keys():
            combinations[i] = combinations[i-1] + combinations[i-2]
        i+=1

    # print(f"combinations: {combinations}")
    return combinations[n-1] + combinations[n-2]



#Recursion : TLE

def climbStairsR(n):

    if n == 1 or n == 2:
        return n
    
    else:

        return climbStairs(n-1) + climbStairs(n-2)


if __name__ == "__main__":

    n = 8 
    print(f"for n == 8  o/p is : {climbStairs(8)} output should be 34")