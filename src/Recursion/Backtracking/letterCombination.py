"""

"""


def letterCombination(digits):

    mappings = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    res = []
    def backtrack(processed,remaining_digits):

        if not remaining_digits:
            res.append(processed)

        else:
            for letter in mappings[remaining_digits[0]]:

                backtrack(processed + letter,remaining_digits[1:])


    backtrack("",digits)

    return res


print(letterCombination("236"))

