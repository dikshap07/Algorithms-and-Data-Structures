def removeElement(nums,val):

    i = 0

    while i<len(nums):

        if nums[i] == val:

            nums.pop(i)

        else:
            i+=1
    print(nums)
    return i

# print(removeElement([2,3,3,4],3))

#without using pop


def removeElement_(nums,val):

    i = 0
    n = len(nums)
    
    while i < n:

        if nums[i] == val:

            nums[i] = nums[n-1]  #if equal replace with last element and reduce len by 1 

            n-=1            #but since we are not increasing i here we check the rpelaced element too

        else:
            i+=1

    return n

print(removeElement_([2,3,3,4],3))