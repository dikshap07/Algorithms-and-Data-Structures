"""
find element in array with recursion - linear search

"""


def isElement(arr,index,k):

    if index >= len(arr): return False #we reached last element and did not find the element


    if arr[index] == k: return True

    return isElement(arr,index+1,k)


def findElement(arr,k):
    return isElement(arr,0,k)


"""
find element in array with recursion - linear search

"""


def isElementIndex(arr,index,k,indices):

    if index >= len(arr): return indices #we reached last element and did not find the element


    if arr[index] == k:
        indices.append(index)
        # return indices

    return isElementIndex(arr,index+1,k,indices)


def findElementIndices(arr,k):
    indices = []
    indices = isElementIndex(arr,0,k,indices)

    return indices


def isElementIndexNL(arr,index,k): #No list argument

    if index >= len(arr): return [] #we reached last element and did not find the element

    if arr[index] == k:
        return index

    return isElementIndex(arr,index+1,k)

def isElementIndexNL(arr, index, k):  # No list argument

    if index >= len(arr): return []  # we reached last element and did not find the element
    index_list = []
    if arr[index] == k:
        index_list.append(index)

    return index_list + isElementIndexNL(arr,index+1,k)

def findElementIndicesNL(arr,k):
    indices = []
    return isElementIndexNL(arr,0,k)



if __name__ == "__main__":

    arr1 = [1,3,4,5,8,31,4]
    k1 = 5
    arr2 = [100]
        # [2,4,5,67,88]
    k2 = 100
    # print(f"find element {k1} in  {arr1} : {findElement(arr1,k1)}")
    # print(f"find element {k2} in  {arr2} : {findElement(arr2,k2)}")

    arr1 = [1, 3, 4, 5, 8, 31, 4,4,4]
    k1 = 4
    arr2 = []
        # [2,4,5,67,88]
    k2 = 100
    print(f"find element {k1} in  {arr1} : {findElementIndicesNL(arr1,k1)}")
    # print(f"find element {k2} in  {arr2} : {findElementIndices(arr2,k2)}")