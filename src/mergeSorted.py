""" Get Median of two sorted arrays
    """

#O(m+n) Solution

def mergeSorted(arr1,arr2):

    p1 = 0
    p2 = 0

    merged = []

    while p1<len(arr1) and p2<len(arr2):

        if arr1[p1] < arr2[p2]:

            merged.append(arr1[p1])
            p1+=1

        else:
            merged.append(arr2[p2])
            p2+=1   

    if p1 == len(arr1):
        merged.extend(arr2[p2:])
    
    else:
        merged.extend(arr1[p1:])

    return merged


def getMedian(arr):
    n = len(arr)

    if n%2==0:

        return (arr[(n//2)] + arr[(n//2)-1])/2

    else:

        return arr[(n//2)]






print(mergeSorted([1,2,3,4],[5,6,7,8,9,9]))        
inp = mergeSorted([2,6,8,8,9,9],[1,2,3,5,7])   
print(inp)
print(getMedian(inp))