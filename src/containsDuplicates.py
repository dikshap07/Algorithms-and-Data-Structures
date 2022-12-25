
"""Return True if given array contains any duplicat elements"""

import collections

def containsDuplicates(nums):

    hash = collections.Counter(nums)


    for key,value in hash.items():

        if value >1:

            return True
    
    return False
