"""Return true is pair sum in a sorted array is equal to given target"""


def isSumTarget(nums, target):  # nums = sorted array of numbers

    left = 0
    right = len(nums) - 1

    while left < right:
        print("nums[left] + nums[right]", nums[left] + nums[right])

        if nums[left] + nums[right] == target:

            return True

        elif nums[left] + nums[right] < target:

            left += 1

        else:

            right -= 1

    return False


print(isSumTarget([1, 2, 4, 6, 8, 9, 14, 15], 13))
