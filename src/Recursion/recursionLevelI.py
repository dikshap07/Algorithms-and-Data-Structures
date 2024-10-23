def reverseString(s):  #no recursion O(1)space


    left,right = 0, len(s)-1
    while left < right:
        s[left],s[right] = s[right],s[left]

        left, right = left+1,right -1

    print(s)
    
 
#using recursion :O(n) space - recursion stack

def reverString(s):

    def helper(left,right):

        if left<right:

            s[left],s[right] = s[right],s[left]

            helper(left+1,right-1)


    helper(0,len(s)-1)
    print(s)


reverString(['h','e','l','l','o'])