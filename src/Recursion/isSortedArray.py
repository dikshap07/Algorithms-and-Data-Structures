"""
USing recursion check if a given array is sorted
"""

def isArrSorted(arr,index):

    if index == len(arr) -1: return True

    return arr[index] < arr[index+1] and isArrSorted(arr,index+1)


def isSorted(arr):
    return isArrSorted(arr,0)



if __name__ == "__main__":
    arr1 = [1,3,4,5,8,31,4]

    arr2 = [2,4,5,67,88]


    print(f"is sorted {arr1} : {isSorted(arr1)}")
    print(f"is sorted {arr2} : {isSorted(arr2)}")