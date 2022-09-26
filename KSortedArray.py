import heapq

def KSortedArray(nums,k):

    sorted_nums = []

    my_heap = []


    for i in range(len(nums)):

        heapq.heappush(my_heap,nums[i]) #adding element to heap

        #heapify
        heapq.heapify(my_heap)

        #if size of heap > k : we pop


        if len(my_heap) > k :

            sorted_nums.append(heapq.heappop(my_heap))

    

        
    return sorted_nums



print(KSortedArray([6,5,3,2,8,10,9],3))




        




