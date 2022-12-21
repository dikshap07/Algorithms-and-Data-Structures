def isMajorityElement(nums, target):
    total_len = len(nums)

    def binarySearch(arr,target):

        s = 0
        e = len(arr)

        while s < e:

            m = (s+e)//2

            if arr[m] == target:

                return m
            
            elif arr[m] < target:
                s = m+1

            else:
                e = m
        return -1

    freq = 0
    found_index = 0

    while found_index!=-1:

        found_index = binarySearch(nums,target)
        if found_index != -1:

            freq+=1
            nums.pop(found_index)

    return freq > (total_len/2)