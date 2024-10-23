

def permutations(proc,unproc):

    if not unproc:
        print(proc)
        return

    #recursion calls to put at eac position

    for i in range(len(proc)):

        first = proc[0:i]
        char = unproc[0]
        end = proc[i:]

        unproc_ = unproc[1:]

        permutations(first+char+end,unproc_)

    return


(permutations(" ","abc"))


"""
Return the permutations in a list: 
"""

def permutations_(proc,unproc,res):

    if not unproc:
        # print(proc)
        res.append(proc)
        return res

    #recursion calls to put at eac position

    for i in range(len(proc)+1):

        first = proc[0:i]
        char = unproc[0]
        end = proc[i:]

        unproc_ = unproc[1:]

        permutations_(first+char+end,unproc_,res)

    return res


# print(permutations_("","abc",[]))
#

"""
Count no of permutations
"""


def permutation_count(unproc):
    count = 0
    res = []

    def permutations(proc,unproc):
        count = 0
        if not unproc:
            count += 1
            res.append(proc)
            print(proc)
            return count


        for i in range(len(proc)+1):
            first = proc[0:i]
            char = unproc[0]
            end = proc[i:]

            count += permutations(first+char+end,unproc[1:])

        return count

    count = permutations("",unproc)

    return res,count

res,count = permutation_count("cbd")
print(f"res: {res}")
print(f"count : {count}")