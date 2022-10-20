import heapq
#using maxHeap


def kClosetOrigin(nums, k):


    maxHeap = []
    kclosest = []


    for i in range(len(nums)):
        
        distance = ((nums[i][0])**2 + (nums[i][1])**2)**(0.5)
        print(f"distance : {distance}, pair : {nums[i]}")

        heapq.heappush(maxHeap,((-1)*distance,nums[i]))


        if len(maxHeap)>k:

            heapq.heappop(maxHeap)


    return [tuple[1] for tuple in maxHeap]

# kClosetOrigin([[0,1],[1,0]],2)
# kClosetOrigin([[1,3],[-2,2]],1)
# kClosetOrigin([[3,3],[5,-1],[-2,4]],2)
kClosetOrigin([[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [1, 1]],1)

