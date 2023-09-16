""" correct Approach: without using division operator
O(n) :Time , #3*O(n):space

"""


def productExceptSelf_(nums):

    size = len(nums)

    L = [1]*size
    R = [1]*size

    #Create the left product array
    
    for i in range(1,size):

        L[i] = L[i-1]*nums[i-1]
    print(f" L: {L}")


    for j in range(size-2,-1,-1):
            R[j] = R[j+1]*nums[j+1]

    print(f"R : {R}")


    res = []

    for i in range(size):

        res.append(L[i]*R[i])

    print(f"res : {res}")

    return res






    #Create the right product array

    return 















"""
Passed but we were not supposed to use division operator
"""
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



    nums = [0,0]
    # [0,2,3,4]
    # 
    #  [0,0]
    output = productExceptSelf_(nums)
    print(f"output: {output}")

