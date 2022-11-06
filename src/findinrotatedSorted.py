def search(nums, target: int):
    def find_pivot(nums):

        l = 0
        r = len(nums)

        while l < r:

            mid = (l + r) // 2

            # case-01

            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:

                return mid

            # case -02

            if nums[mid] < nums[mid - 1]:

                return mid - 1

            # ignoring right side of the array since we want largest num and in this case everything to right of mid will be smaller than mid

            if nums[mid] < nums[l]:

                r = mid

            # ignore left side of the array
            else:

                l = mid + 1

        return -1

    def binary_search(nums, start, end, target):

        while start < end:

            mid = (start + end) // 2

            if nums[mid] == target:

                return mid

            elif nums[mid] < target:

                start = mid + 1

            else:

                end = mid

        return -1

    pivot = find_pivot(nums)

    output = binary_search(nums, 0, pivot + 1, target)

    if output == -1:

        output = binary_search(nums, pivot + 1, len(nums), target)

    return output


# arr = [4, 5, 6, 7, 0, 1, 2]
# target = 7

# arr = [1]
# target = -1

arr = [5, 1, 3]
target = -1

print(f"{arr}, target index = {search(arr,target)}")
