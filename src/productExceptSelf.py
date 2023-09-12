

def productExceptSelf(nums):


    hash = {}
    product = nums[0]
    if nums[0] == 0:
        product = 1
        hash[0] = 0
    res = []

    #to calculate the product of all the elements inthe array
    for i in range(1,len(nums)):


        if nums[i] == 0:
            # product = 0
            hash[i] = 0
            continue


        product = product*nums[i]

        print(f"product in loop: {product}")

    print(f"product at the end: {product}")

    print(f"hash: {hash}")
    #when we have a zero in the arrau

    if hash: #implies we have indices with zero in them
        if len(hash) > 1:
            res = [0 for i in range(len(nums))]

        else:
            res = [0 if i not in hash else product for i in range(len(nums))]
        return res

    #to update the result array

    for i in range(len(nums)):

        res.append(int(product/nums[i]))


    return res


if __name__ == "__main__":



    nums = [0,2,3,4]
    # [-1,1,0,-3,3]
    #  [0,0]
    output = productExceptSelf(nums)
    print(f"output: {output}")

