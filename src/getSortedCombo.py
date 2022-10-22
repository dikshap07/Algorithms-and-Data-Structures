def getSortedCombo(arr1, arr2):

    p1 = 0
    p2 = 0

    output = []
    while p1 < len(arr1) and p2 < len(arr2):

        if arr1[p1] < arr2[p2]:

            output.append(arr1[p1])
            p1 += 1

        else:

            output.append(arr2[p2])
            p2 += 1

    while p2 < len(arr2):

        output.append(arr2[p2])
        p2 += 1

    while p1 < len(arr1):

        output.append(arr1[p1])
        p1 += 1
    # print(output)

    return output


print(getSortedCombo([1, 4, 7, 20, 28], [3, 5, 6, 7]))
