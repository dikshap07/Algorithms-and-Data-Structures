import math

#Using Dynamic Programming, Kadane's Algorithm


def maxSubArray(nums):

    curr_subarray = nums[0]
    max_subarray = nums[0]


    for num in nums[1:]:

        curr_subarray = max(num,curr_subarray + num)
        max_subarray = max(curr_subarray,max_subarray)

    return max_subarray

            






nums = [-2,1,-3,4,-1,2,1,-5,4]
# [1,2,-1,-2,2,1,-2,1,4,-5,4]

# [1]
# 

# print(maxSubarray(nums))

# print(sum(nums[:8])) 


# print(nums[3:9])

# def maxSubArray(nums) -> int:
#     max_subarray = -math.inf
#     for i in range(len(nums)):
#         current_subarray = []
#         for j in range(i, len(nums)):
            
#             current_subarray.append(nums[j])
            
#             max_subarray = max(max_subarray, sum(current_subarray))
#             print(f"current_subarray {current_subarray} and sum = {sum(current_subarray)}")
    
#     return max_subarray

print(maxSubArray(nums))


#latest recursion attempt


def maxSubArray(self, nums: List[int]):

    max_sum = sum(nums)
    arr = nums

    def maxSum(thearray,max_sum):

        print(f"in maxSUm thearray: {thearray}")
        print(f"in maxSUm max_sum: {max_sum}")

        if len(thearray)==1:
            print(f"in len 1 array: {thearray}")
            max_sum = max(max_sum,thearray[0])
            print(f"in len 1 array sum : {max_sum}")
            return (thearray,max_sum)
        else:
            #left 

            left_arr = thearray[1:]
            left_sum = sum(left_arr)

            #right 

            right_arr = thearray[:-1]
            right_sum = sum(right_arr)


            if left_sum > right_sum:
                print(f"left array btter")
                max_sum = max(left_sum,max_sum)

                arr, max_sum = maxSum(left_arr,max_sum)

            elif  left_sum < right_sum:
                print(f"right array btter")
                max_sum = max(right_sum,max_sum)

                arr, max_sum = maxSum(right_arr,max_sum)

            else:
                print(f"both arrays equal")
                arr, max_sum_left = maxSum(left_arr,max(left_sum,max_sum))
                arr, max_sum_right = maxSum(right_arr,max(left_sum,max_sum))

                max_sum = max(max_sum,max_sum_left,max_sum_right)

            return arr,max_sum

        
    res, res_sum = maxSum(arr,max_sum)

    return res_sum




#My wrong attempt:  #9 omnths ago

# def maxSubarray(nums):


#     total_sum = sum(nums)

#     # to check for subarray

#     start,end = 0,len(nums)
   

#     max_start,max_end = 0,len(nums)
    

#     while len(nums[start:end]) > 1:
#         print("\n")
#         print(f"new loop with total_sum = {total_sum} start = {start} and end = {end}")
#         print(f" max strat = {max_start} and max_end = {max_end}")


#         #check left subarray

#         sum_left = sum(nums[start+1:end])
#         print(f" sum_left =  {sum_left} for {nums[start+1:end]}")
        
#         #check right subarray

#         sum_right = sum(nums[start:end-1])
#         print(f" sum_right =  {sum_right} for {nums[start:end-1]}")

#         #checking sum

#         if sum_left > sum_right:

            
#             print(" in left")
            

#             if sum_left >= total_sum:
            
#                 total_sum = sum_left

#                 max_start = start
#                 max_end = end-1
            
#             start += 1

#         elif sum_right > sum_left:
            
#             print("in right")

#             if sum_right >= total_sum:
            
#                 total_sum = sum_right
#                 max_end = end-1
#                 max_start = start
            
            
#             end -=1

#         elif sum_right == sum_left:
#             print("\n")
#             print("Subarray sum equal")

#             a = sum(nums[start+1:end])
#             print(f" sum_right =  {a} for {nums[start+1:end]}")
#             b = sum(nums[start:end-1])
#             print(f" sum_left =  {b} for {nums[start:end-1]}")

#             if a > b:
                

#                 if a > total_sum:
#                     total_sum = a
#                     max_start = start


#                 start += 1
                
            
#             else:
                
#                 if b > total_sum:
#                     total_sum = b
#                     max_end = end             

#                 end -=1
                

#     return nums[max_start:max_end], total_sum