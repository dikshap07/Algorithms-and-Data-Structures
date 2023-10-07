
#get count of triplets in an array woth sum < taregt


"""Two pointer  approach : O(n*n)"""
def threeSumSmaller(nums, target: int) -> int:
    res_count = 0
    nums.sort()
    

    for i in range(len(nums)):

        left,right = i+1,len(nums)-1 #because we only want to checright numbers to the right of current =number

        while left < right:

            sum = nums[i] +nums[left] + nums[right]

            if sum < target:

                res_count += (right-left) #because if i,left,right worright then ileft,right-1; i,left,right-2..i,left,left+1 will worright i.e right-left pairs 
                left+=1 #lets checright for i,left+1,right and less
            
            else:
                #sum is more to we reduce right, coz we want smaller numbers than nums[right]
                right-=1

    return res_count

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(threeSumSmaller(nums,1))