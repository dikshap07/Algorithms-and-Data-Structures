

'''given (n,m) return the num of unique ways you can reach from left top corner to bottom right corner
constraints: can only move down or right at one point'''


def unique_paths(n,m):

    if n == 1 or m == 1:

        return 1

    else:
        return unique_paths(n-1,m) + unique_paths(n,m-1)


print(unique_paths(2,4))


