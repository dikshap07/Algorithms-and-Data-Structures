
"""
Problem 1 : Given a string print all the subsets in it
"""


def subset(processed,unprocessed):

    if unprocessed == "":
        print(processed) #we noticed that subset is when unprocessed is ""
        return #we need to break out of this fucntion call

    #take teh first char of unprocessed, at each we have 2 choices -to add or to ignore
    char = unprocessed[0]
    subset(processed + char,unprocessed[1:])
    subset(processed + "", unprocessed[1:])

s = "abc"
# print(f"subsets of {s} : {subset("",s)}")


"""
Problem 2 : Given a string return an array with all its subsets
"""


def subset_array(processed,unprocessed,out):

    if unprocessed == "":
        # print(processed) #we noticed that subset is when unprocessed is ""
        out.append(processed)
        # print(out)
        return out#we need to break out of this fucntion call

    #take teh first char of unprocessed, at each we have 2 choices -to add or to ignore
    char = unprocessed[0]
    subset_array(processed + char,unprocessed[1:],out)
    subset_array(processed + "", unprocessed[1:],out)

    return out

#Improved - Time complexity - O(n*2^n)
def subset_array(processed,unprocessed,out):

    if unprocessed == "":
        # print(processed) #we noticed that subset is when unprocessed is ""
        out.append(processed)
        # print(out)
        return #we need to break out of this function, but no need to retrun anything because modifing out inplace

    #take teh first char of unprocessed, at each we have 2 choices -to add or to ignore
    char = unprocessed[0]
    subset_array(processed + char,unprocessed[1:],out)
    subset_array(processed, unprocessed[1:],out) #no point of + "" -doesnt change processed

    return out

#Improved and cleaner time complexity - O(n*2^n)
def subset_array_eff(processed,unprocessed):

    #base case
    if unprocessed== "":
        return [processed]

    char = unprocessed[0]
    included_char = subset_array_eff(processed + char,unprocessed[1:])
    excluded_char = subset_array_eff(processed,unprocessed[1:])

    return included_char + excluded_char

s = "abc"
print(f"subsets of {s} : {subset_array_eff("",s)}")


"""
Problem : All subsets and thE ASCII value of their chars
"""

def subset_array_ASCII(processed,unprocessed):

    #base case
    if unprocessed== "":
        ascii = [ord(char) for char in processed]
        return [{processed: ascii}]

    char = unprocessed[0]
    included_char = subset_array_ASCII(processed + char,unprocessed[1:])
    excluded_char = subset_array_ASCII(processed,unprocessed[1:])

    return included_char + excluded_char

s = "abc"
print(f"subsets of {s} : {subset_array_ASCII("",s)}")