def binarysearch(arr, start, end, target):

    while start < end:

        mid = (start + end) // 2

        if arr[mid] == target:

            return mid

        elif arr[mid] < target:

            start = mid + 1

        else:

            end = mid

    return -1


print(binarysearch([1, 2, 3], 0, 3, 3))
