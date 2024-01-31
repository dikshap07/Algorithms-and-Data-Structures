#take pivot, get left subarray <pivot, right subarray > pivot call quicksort recursively
#hint : think basee case
#best O(nlogn)
#worsr : O(n*2) 
def quicksort(nums):

    if len(nums) == 1 or len(nums) == 0:
        return nums
    
    pivot = nums[(len(nums)//2)] #middle element as pivot here
    left_sub,right_sub = [],[]
    for i in range(len(nums)):
        if i != (len(nums)//2):
            if nums[i] < pivot:
                left_sub.append(nums[i])
            
            elif nums[i] > pivot:
                right_sub.append(nums[i])
        
    return quicksort(left_sub) + [pivot] + quicksort(right_sub)


if __name__ == "__main__":

    nums = [6,2,1,5,4,3]
    print(quicksort(nums))


