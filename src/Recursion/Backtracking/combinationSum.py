"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""



def combinationSum(candidates,target):

    results = []
    def getCombinations(processed,candidates,start):

        if sum(processed) == target:
            results.append(processed[:])
            return

        if sum(processed)> target:
            return

        for index in range(start,len(candidates)):

            processed.append(candidates[index])
            if sum(processed)<= target:
                getCombinations(processed,candidates,index)

            processed.pop()


    getCombinations([],candidates,0)

    return results



print(combinationSum([2,3,6,7],7))
#expected : [[2, 2, 3], [7]]
