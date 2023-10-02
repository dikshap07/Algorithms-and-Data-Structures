""" 
Find min in a rotated sorted array
"""



def findMin( nums):

    #check if array is rotated
    if nums[0] < nums[-1] or len(nums)==1:
        print(f"array not rotated")
        return nums[0]
    
    #otherwise
    #calculate mid

    start = 0
    end = len(nums)-1

    while start <= end:

        mid = start+ (end-start)// 2

        

        if nums[mid]>nums[mid+1]: # implies  this is the descinding point so nums[mid+1] is the min
            return nums[mid+1]
        
        if nums[mid-1] > nums[mid]: # implies  this is the descinding point so nums[mid] is the min
            return nums[mid]

        #condition 1: if mid > nums[0] -> we search iin the right array
        if nums[mid] > nums[0]:

            start = mid+1
        #condition 2: if mid < nums[0] -> we search iin the left array
        else:

            end = mid - 1



if __name__ == "__main__":

    nums = [3,4,5,1,2]
    nums = [4,5,6,7,0,1,2]
    nums = [1,2,3,4,5,6]

    print(f"min for array: {nums} is : {findMin(nums)}")