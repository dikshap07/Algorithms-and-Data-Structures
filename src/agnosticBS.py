# Python program for the above approach

# An iterative binary search function.

'''here end = len(arr) - 1'''
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


'''If you dont want to use <= when updating end it will be equal to mid and not mid -1 '''
def binarySearch_my(arr, start, end, x):

    # Checking the sorted order of the given array
    isAsc = arr[start] < arr[end-1]

    while start < end:
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
                end = middle

        # Descending order
        else:

            # If x smaller, ignore left half
            if arr[middle] > x:
                start = middle + 1

            # If x greater, ignore right half
            else:
                end = middle 

    # Element is not present
    return -1


# Driver Code
arr = [0,1,2,3,5,4,3, 2]
x = 3
n = len(arr)
print(f'binarySearch({arr}, 4, 7, target = {x}) output:  {binarySearch(arr, 4, 7, x)}')
print(f'binarySearch_my({arr}, 4, 8,target = {x}) output: {binarySearch_my(arr, 4, 8, x)}')