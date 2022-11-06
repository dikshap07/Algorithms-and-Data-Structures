def search_Range(nums, target):

    ans = [-1, -1]

    def search(nums, target, findFirstOccurence):
        ans_ = -1
        l = 0
        r = len(nums)

        while l < r:

            mid = (l + r) // 2

            if nums[mid] < target:

                l = mid + 1

            elif nums[mid] > target:

                r = mid

            else:

                ans_ = mid

                if findFirstOccurence:

                    r = mid

                else:

                    l = mid + 1
        return ans_

    ans[0] = search(nums, target, True)

    if ans[0] != -1:

        ans[1] = search(nums, target, False)

    return ans


print("\n")
print(search_Range([5, 7, 7, 8, 8, 10], 8))
print("\n")
print(search_Range([5, 7, 7, 8, 8, 10], 2))
print("\n")
print(search_Range([5, 7, 7, 8, 8, 10], 5))
print("\n")
print(search_Range([7, 7, 7, 7, 7, 7], 7))


def searchRange(nums, target):

    start = end = -1
    # find first occurence
    l = 0
    r = len(nums)
    while l < r:

        mid = (l + r) // 2

        if nums[mid] == target:

            r = mid
            start = mid

        elif nums[mid] < target:

            l = mid + 1

        else:

            r = mid

    # find
    # last occurence
    l = 0
    r = len(nums)

    while l < r:
        mid = (l + r) // 2

        if nums[mid] == target:

            l = mid + 1
            end = mid

        elif nums[mid] < target:

            l = mid + 1

        else:

            r = mid

    return [start, end]


# def searchRange(nums, target: int):

#     if len(nums) == 0:
#         return [-1, -1]

#     l, r = 0, len(nums)

#     start = end = (l + r) // 2

#     while l < r:

#         mid = (l + r) // 2

#         if nums[mid] == target:

#             if nums[mid - 1] != target:

#                 l = mid + 1
#                 start = mid
#                 continue

#             else:
#                 start = mid - 1
#                 r = mid

#             if nums[mid + 1] != target:

#                 r = mid
#                 end = mid
#                 continue

#             else:
#                 end = mid + 1
#                 l = mid + 1

#         # if nums[mid] == target:

#         #     if nums[min(start, mid)] == target:
#         #         start = min(start, mid)

#         #     else:
#         #         start = mid

#         #     if nums[max(end, mid)] == target:

#         #         print("end updated")

#         #         end = max(end, mid)

#         #     else:
#         #         end = mid

#         #     print("end not updated")

#         #     l = mid + 1

#         elif nums[mid] < target:

#             l = mid + 1

#         else:

#             r = mid

#     if start == end == ((0 + len(nums)) // 2) and nums[start] != target:

#         return [-1, -1]

#     else:

#         return [start, end]
