"""Group by character approach : 2*O(n) runtime i.e. O(n) runtime"""


def countBinarySubstrings(s):
    groups = []

    counter = 1
    zero_substring_count = 0

    i = 1
    while i < len(s):
        # print(i)
        if s[i] == s[i - 1]:
            counter += 1

        else:
            groups.append(counter)

            counter = 1

        i += 1
    groups.append(counter)

    for i in range(0, len(groups) - 1):
        zero_substring_count += min(groups[i], groups[i + 1])

    return zero_substring_count


"""O(n) approach """


def countBinarySubstrings(s):
    curr = 0
    prev = 0
    ans = 0
    curr_char = None

    for c in s:
        if curr_char != c:
            prev = curr
            curr_char = c
            curr = 1

        else:
            curr += 1

        if curr <= prev:
            ans += 1

    return ans


"""Without storing groups, just storing 3 elements of groups, O(n) Time Complexity"""


def countBinarySubstrings(self, s):
    ans, prev, cur = 0, 0, 1
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            ans += min(prev, cur)
            prev, cur = cur, 1
        else:
            cur += 1

    return ans + min(prev, cur)  # +min(prev,cur) for the last 2 groups


if __name__ == "__main__":
    s = "10101"

    print(countBinarySubstrings(s))
