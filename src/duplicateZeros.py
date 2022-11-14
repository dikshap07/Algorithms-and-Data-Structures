
def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """

    possible_dups = 0
    len_ = len(arr) - 1 #last index

    for pointer in range(len_+1):  #so that it goes till last index

        if pointer > len_ - possible_dups:
            #len_ - possible_dups : tells us the number of elements from og array that will be retained, so we dont need to check after these
            break

        if arr[pointer] == 0:

            #edge case: if last element of new array is 0, we dont need to duplicate that cz no space 
            if pointer == len_ - possible_dups:

                arr[len_] = 0 #so we just copy it as it is at the last position
                len_ -= 1 #and then only elements before it are considered
                break
            
            #otherwise we count that 0 as it needs to be duplicated
            possible_dups+=1

    last = len_ - possible_dups

        #now changing the array

    for i in range(last,-1,-1):

        #if we encounter 0: we change i+possible_dups index to zero
        if arr[i] == 0:

            arr[i+possible_dups] = 0
            #decrease num of zeros that need to be duplicates by 1
            possible_dups-=1
            arr[i+possible_dups] =  0 #the duplicated zero

        else:

            arr[i+possible_dups] = arr[i]


#Brute Force - O(n**2)

def duplicateZeros(arr):
        
        # left = 0
        
        
    while left< len(arr)-1:
        # print("left",left)
        
        if arr[left] == 0:
            # print("left: ",left)
            
            def shift_array(end,start):
                #end = len(arr)-1
                #start = left+1
            
                for i in range(end,start,-1):
                    print(i)
                # print(f"arr[i]: {arr[i]}-> arr[i-1] : {arr[i-1]}")
                    arr[i] = arr[i-1]
                # print(f"arr[i]: {arr[i]}-> arr[i-1] : {arr[i-1]}")
            arr[left+1] = 0
            # print("arr",arr)
                
            left+=2
            
        else:
            left+=1
        