def searchInInfArray(infarray, target):

    start = 0
    end = 1

    while infarray[end] < target:
        print("\n")
        print("start : ", start)
        print("end: ", end)

        new_start = end + 1

        end = end + (end - start + 1) * 2  # double the size of chunk

        start = new_start

    if infarray[end] >= target:

        return binarysearch(infarray, target, start, end)


def binarysearch(arr, target, l, r):

    while l <= r:

        mid = (l + r) // 2

        if arr[mid] == target:

            return mid

        elif arr[mid] < target:

            l = mid + 1

        else:
            r = mid - 1

    return -1


print(
    f"{[3,5,7,9,10,19,20,21,23,25,27,28,29,30,31,32]} , {searchInInfArray([3,5,7,9,10,19,20,21,23,25,27,28,29,30,31,32],27)}"
)

# print(binarysearch([1, 2, 3, 4, 5], 0))
