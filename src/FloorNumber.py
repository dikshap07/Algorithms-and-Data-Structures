def floor(arr, target):

    l = 0
    r = len(arr)

    floor = arr[0]

    if target < arr[0]:

        return "no solution"

    while l < r:

        mid = (l + r) // 2

        if arr[mid] == target:

            return target

        elif arr[mid] > target:

            r = mid

        else:

            l = mid + 1
            floor = max(floor, arr[mid])

    return floor


print(floor([2, 3, 5, 9, 14, 16, 18], 14))
print(floor([2, 3, 5, 9, 14, 16, 18], 17))
print(floor([2, 3, 5, 9, 14, 16, 18], 4))
print(floor([2, 3, 5, 9, 14, 16, 18], 1))
print(floor([2, 3, 5, 9, 14, 16, 18], 19))
print(floor([2, 3, 5, 9, 14, 16, 18], 3))
