# Python program for the above approach

# An iterative binary search function.
def binarySearch(arr, start, end, x):

    # Checking the sorted order of the given array
    isAsc = arr[start] < arr[end]

    while start <= end:
        middle = start + (end - start) // 2

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


# Driver Code
arr = [0, 5, 2]
x = 10
n = len(arr)
print(binarySearch(arr, 0, 1, 0))
