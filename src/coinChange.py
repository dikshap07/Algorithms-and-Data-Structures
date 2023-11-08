
"""
given : array  of coin denominations, amount 
return : min number of coins needed to reach the amount else return -1
"""


#DFS, Backtracking + Memoization Solution


def coinChange(amount,coins):

    memory = {} #outside because we need to keep track of it

    def dfs(remaining_amount):

        if remaining_amount in memory:

            return memory[remaining_amount]


        if remaining_amount == 0:  #base case

            return 0

        min_coins = float('inf')

        for coin in coins:

            if remaining_amount >= 0:

                sub_problem = dfs(remaining_amount-coin) #for each coin we will check the dfs if one coin of this value is taken

                if sub_problem != -1:

                    min_coins = min(min_coins , sub_problem+1)

        
        memory[remaining_amount] = min_coins if min_coins != float('inf') else -1

        return memory[remaining_amount]

    result =  dfs(amount)

    return result if result != float('inf') else -1

