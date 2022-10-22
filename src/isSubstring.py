def isSubstring(s, t):

    i = 0

    while i < len(s) and j < len(t):

        if s[i] == s[j]:

            i += 1

        j += 1

    return i == len(s)


print(isSubstring("ace", "abcde"))
