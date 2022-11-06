def findInMountainArray(target: int, mountain_arr):

    l = 0
    r = len(mountain_arr)

    def binary_search(arr, start, end, x):

        # Checking the sorted order of the given array
        isAsc = arr[start] < arr[end]

        while start <= end:
            middle = (start + end) // 2

            # Check if x is present at mid
            if arr[middle] == x:
                return middle

            # Ascending order
            if isAsc == True:

                # If x greater, ignore left half
                if arr[middle] < x:
                    start = middle + 1

                # If x smaller, ignore right half
                else:
                    end = middle - 1

            # Descending order
            else:

                # If x smaller, ignore left half
                if arr[middle] > x:
                    start = middle + 1

                # If x greater, ignore right half
                else:
                    end = middle - 1

        # Element is not present
        return -1

    while l < r:

        mid = (l + r) // 2

        if mountain_arr[mid] > mountain_arr[mid + 1]:

            # descending half
            # if in descendig half we check in the left subarray

            r = mid - 1
            print(f"start = {l} end = {r}")

            # if we find target in left half we dont need to check right half
            # because index of right half will be greater than this so we automatically
            # discard that

        else:
            # if either we already in ascending half or
            # if we did not find target in left half
            # we check for target in right half

            l = mid + 1

    output = binary_search(mountain_arr, 0, l, target)

    if output == -1:

        output = binary_search(mountain_arr, l, len(mountain_arr) - 1, target)

    return output


print(findInMountainArray(5, [1, 5, 2]))
