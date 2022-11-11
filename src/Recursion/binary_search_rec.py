def binary_search_rec(arr,target,s,e):

    if s > e:

        return -1


    mid = (s + e)//2

    if arr[mid] == target:

        return mid
    
    if arr[mid] < target:

        return binary_search_rec(arr,target,mid+1,e)

    return binary_search_rec(arr,target,s,mid)


print(binary_search_rec([1,2,3,4,5],7,0,4))