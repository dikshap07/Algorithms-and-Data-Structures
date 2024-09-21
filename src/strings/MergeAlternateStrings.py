
def mergeAlternately(self, word1: str, word2: str) -> str:
    "Two pointer approach"

    l1 = len(word1)
    l2 = len(word2)

    i = k = 0
    merged = []

    if l1< l2:

        while i< l1:

            merged.append(word1[i])
            merged.append(word2[i])
            i +=1
            k+=1

        merged.append(word2[k:])

    else:

        while k< l2:

            merged.append(word1[i])
            merged.append(word2[i])
            i +=1
            k+=1

        merged.append(word1[i:])

    return "".join(merged)

    def mergeAlternately(self, word1: str, word2: str) -> str:

        "Single pointer approach"

        l1 = len(word1)
        l2 = len(word2)

        i = 0
        merged = []

        while i < min(l1,l2):

            merged.append(word1[i])
            merged.append(word2[i])
            i+=1

        if l1< l2:
            merged.append(word2[i:])
        
        else:
            merged.append(word1[i:])

        return "".join(merged)