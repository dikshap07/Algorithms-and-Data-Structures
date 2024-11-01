"""
Given an array of integers candidates and a target integer target,
return a list of all unique combinations of candidates where
the chosen numbers sum to target. You may return the combinations in any order.

"""

def combinationSum2(candidates, target: int):

    results = []

    def getCombinations(processed, candidates, start):

        if sum(processed) == target:

            results.append(processed[:])

            return

        elif sum(processed) > target:
            return

        # while start < len(candidates):
        for index in range(start, len(candidates)):

            if index>start and candidates[index] == candidates[index-1]:
                continue

            processed.append(candidates[index])

            if sum(processed) <= target:
                getCombinations(processed, candidates, index+1)
            # start+=1

            processed.pop()

    candidates.sort()
    getCombinations([], candidates, 0)

    return results


print(combinationSum2([10,1,2,7,6,1,5],8))