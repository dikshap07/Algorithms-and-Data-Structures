"""
Problem: get the subsequence / subsets from a given array in orderm using iteration
"""


def subSequence(arr):
    res = [[]]
    if not arr:

        return res
    i = 0

    while  i < len(arr):
        curr = arr[i]

        new_subs = []
        for ele in res:
            new_subs.append(ele + [curr])

        res.extend(new_subs)
        i+=1

    return res


# print(subSequence([1,2,3]))


"""
To take care of duplicate elements - using sets
"""

def subSeq(arr):

    res = {()}

    if not arr:
        return list(res)

    i = 0
    while i<len(arr):

        curr = arr[i]

        new_subsets = set()
        for ele in res:

            new_subsets.add(ele + (curr,))

        res.update(new_subsets)
        i+=1

    res = [list(ele) for ele in res]

    return res


# print(f" : {subSeq([1,2,2])}")



"""
Desaling with duplicates: we can say if we have a duplicate element we dont need to add this element to all of teh subsets
we only need to add it to the new subsets from the last generated subsets(this is when the duplicates are adjacent),
so we will have to sort the initial array
"""

def subSeqDuplicates(arr):
    res = [[]]

    if not arr:
        return res
    #sort the input
    arr.sort()

    end = 0
    for i,num in enumerate(arr):
        start = 0

        if i > 0 and arr[i] == arr[i-1]:
            start = end + 1 #end will be the no of subsets added last time
        subsets = []
        for j in range(start,len(res)):

            subsets.append(res[j] + [num])

        end = len(subsets)-1

        res.extend(subsets)

    return res



print(f"dealing w duplicates using pointers: {subSeqDuplicates([1,2,2])}")









