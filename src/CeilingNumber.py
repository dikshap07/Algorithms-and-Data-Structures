def ceiling(arr, target):

    l = 0
    r = len(arr)

    ceil = arr[-1]
    if target > arr[-1]:
        return -1

    while l < r:

        mid = (l + r) // 2

        if arr[mid] == target:

            return target

        elif arr[mid] < target:

            l = mid + 1

        else:

            r = mid
            ceil = min(ceil, arr[mid])

    return ceil


print(ceiling([2, 3, 5, 9, 14, 16, 18], 14))
print(ceiling([2, 3, 5, 9, 14, 16, 18], 17))
print(ceiling([2, 3, 5, 9, 14, 16, 18], 4))
print(ceiling([2, 3, 5, 9, 14, 16, 18], 1))
print(ceiling([2, 3, 5, 9, 14, 16, 18], 19))
print(ceiling([2, 3, 5, 9, 14, 16, 18], 3))
