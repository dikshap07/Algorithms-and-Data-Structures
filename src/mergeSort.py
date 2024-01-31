


def mergeSort(arr):  #will split the array and sort them

    if len(arr) == 0 or len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    return merge(mergeSort(left),mergeSort(right))

def merge(a1,a2): #takes input sorted arrays
    merged = []
    while a1 and a2:  #until both of thwm are empty

        if a1[0] < a2[0]:
            merged.append(a1[0])
            a1.pop(0)

        else:
            merged.append(a2[0])
            a2.pop(0)

    if not a1:
        for num in a2:
            merged.append(num)

    if not a2:
        for num in a1:
            merged.append(num)
    return merged

if __name__ == "__main__":

    nums = [6,20,1,5,4,3,3,12]
    print(mergeSort(nums))

    # a = [1,3,5]
    # b = [2,4]

    # print(merge(a,b))