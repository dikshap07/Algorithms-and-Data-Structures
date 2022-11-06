def peakMountainArray(arr):

    start = 0
    end = len(arr) - 1

    while start < end:

        mid = (start + end) // 2

        if arr[mid] > arr[mid + 1]:

            # print("left half")

            end = mid
            # print(f"start : {start} and end : {end}")

        else:

            # print("right half")

            start = mid + 1

            # print(f"start : {start} and end : {end}")

    # print(f"start : {start} and end : {end}")
    return start


arr_ = [1, 2, 2, 4, 5, 3, 1]
print(arr_)

print(f"{arr_ }: {peakMountainArray(arr_)}")


# brute force - O(n)
# def peakMountainArray(arr):

#     return arr.index(max(arr))
