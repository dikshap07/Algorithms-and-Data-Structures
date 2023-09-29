

#get the max product of a subarray in an integer array

"""Dynamic programming solution"""

def maxProductSubarray(nums):

    res = min_so_far = max_so_far = nums[0]


    #min_so_far = to keep track of all the neg numbers properly in the product
    #max_so_far =  to keep trackl of all positive number product
    
    for num in nums[1:]:

        curr = num
        min_last = min_so_far

        min_so_far = min(curr,min_so_far*curr,max_so_far*curr)
        print(f"min_so_far: {min_so_far}")
        max_so_far = max(curr,min_last*curr,max_so_far*curr)
        print(f"max_so_far: {max_so_far}")

        res = max(res,max_so_far)
        print(f"res:{res}")

    return res


if __name__ == "__main__":

    nums = [2,3,-2,4]
    nums = [0,0,0,0,9]
    nums = [0,0,-1,-2,9,9]
    nums = [0,0,-1,0,9,-9]
    print(maxProductSubarray(nums))