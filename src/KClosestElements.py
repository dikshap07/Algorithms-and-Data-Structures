import heapq

# using maxHeap


def KClosest(nums, x, k):
    maxHeap = []

    for i in range(len(nums)):
        heapq.heappush(maxHeap, ((-1) * abs(nums[i] - x), nums[i]))

        if len(maxHeap) > k:
            heapq.heappop(maxHeap)

    return [closest[1] for closest in maxHeap]


# KClosest([5,6,7,9,10],7,3)
# print(KClosest([5, 6, 7, 8, 9], 7, 3))
