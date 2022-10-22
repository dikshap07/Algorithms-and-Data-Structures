# checking palindrom using 2 pointers for only alpha numeric characters

import re


def isPalindrome(s):

    s = s.lower()
    new_s = re.sub("[^A-Za-z0-9]+", "", s)

    left = 0
    right = len(new_s) - 1

    while left < right:

        if new_s[left] != new_s[right]:

            return False

        left += 1
        right -= 1

    return True


# my first attempt

# def isPalindrome(s):

# left = 0

# right = len(s) - 1

# palindrome = False

# if right == 1 or right == 0:

#     return True

# else:

#     while left < right:

#         if s[left] == s[right]:

#             palindrome = True
#             left += 1
#             right -= 1


#         else:

#             return False

# return palindrome


# print(isPalindrome("theht"))
print(isPalindrome("A man, a plan, a canal: Panama"))

# print(isPalindrome("raceacar"))
