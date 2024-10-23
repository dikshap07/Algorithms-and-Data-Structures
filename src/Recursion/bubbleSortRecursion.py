def bubbleSort(arr, r, c):
    """
    Think of this as, as we decrease row, we only check upto certain index, because before we change row we would have
    made the largest element reach the last position, then second last and so on, so c not reaching/checking until teh end
    is fine.
    """
    if not arr or r == 0:
        return arr

    if c < r: #becayse we want it to be less than len(arr) -1 because we are checking c+1
        if arr[c + 1] < arr[c]:
            #swap
            next, curr = arr[c + 1], arr[c]
            arr[c], arr[c + 1] = next, curr

        return bubbleSort(arr, r, c + 1)

    else:
        return bubbleSort(arr, r - 1, 0)


print(bubbleSort([5,3,8,4,2,1,1],6,0))