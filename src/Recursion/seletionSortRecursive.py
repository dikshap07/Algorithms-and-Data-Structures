from tempfile import tempdir


def selectionSortRecursive(arr,r,c,max_,max_index):

    "take the largest element in the array and swap it with the last element"

    if r == 1 or not arr: return arr

    if c< r:
        if max_ <= arr[c]:
            max_index = c
            max_ = arr[c]

        return selectionSortRecursive(arr,r,c+1,max_,max_index)

    else:

        last = arr[r-1]
        arr[max_index] = last
        arr[c] = max_
        print(f"arr: after swap: {arr}")
        return selectionSortRecursive(arr,r-1,0,float("-inf"),-1)

arr = [9, 1, 5, 3, 5, 5, 8]
# arr = [5,4,3,2,1]
print(selectionSortRecursive(arr,6,0,float("-inf"),-1))