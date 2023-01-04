#Two Pass Hash Map

def twoSums(nums,target)
    hash = {}
    for i,num in enumerate(nums):
        hash[num]= i

    for i,num in enumerate(nums):

        diff = target - num

        if diff in hash and hash[diff] != i:

            return [i,hash[diff]]

#Single Pass Hash Map

def twoSums(nums,target):

    hash = {}

    for i,num in enumerate(nums):

        diff = target - num

        if diff in hash:

            return [i,hash[diff]]

        hash[num] = i


