

def search2DMatrix(mat,target):


    def binarySearch(array,target):

        start = 0
        end = len(array)

        while start < end:

            mid = start + (end - start)//2


            if array[mid] == target:

                return True

            elif array[mid] < target:

                start = mid +1


            else:
                end = mid
        
        return False


    for row in mat:

        if target < mat[-1]:

            return binarySearch(row,target)


    return False

