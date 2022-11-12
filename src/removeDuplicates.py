#output -> k and arr






""" Brute Force : O(N) """

def removeDuplicates(arr):

    i = 0

    while i < len(arr)-1:

        if arr[i] == arr[i+1]:
            arr.pop(i)
            print("brea",arr)
        else:
            i +=1

    k = len(arr)

    return k,arr




# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(removeDuplicates([1,1,2]))
# print(removeDuplicates([2]))


def removeDuplicates_(arr):

    left =  right = 1

    while right < len(arr):

        if arr[right] != arr[right-1]:
            arr[left] = arr[right]
            left +=1

        right+=1

    return left

print(removeDuplicates_([0,0,1,1,1,2,2,3,3,4,5,6,7]))


