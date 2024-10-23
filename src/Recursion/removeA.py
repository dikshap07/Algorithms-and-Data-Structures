"""
Given a string use recursion to remove all "a"s from it
"""


def removeA(s,i,ans):

    if (i>= len(s)) or not s: return ans

    if s[i] != "a":
        ans+=s[i]
        return removeA(s,i+1,ans)

    return removeA(s,i+1,ans)

#method 2
def removeA(s,i):

    if (i>= len(s)) or not s: return ""

    if s[i] != "a":
        # ans+=s[i]
        return s[i] + removeA(s,i+1)

    return "" + removeA(s,i+1)


print(removeA("babbascsa",0))

