"""O(m+n): Time Complexity
O(m) : Space Complexity"""


def merge(nums1, m, nums2, n):

    num1copy = nums1[:m]

    p1 = p2 = 0

    for p in range(m + n):

        if p2 >= n or (p1 < m and num1copy[p1] < nums2[p2]):

            nums1[p] = num1copy[p1]
            p1 += 1

        else:

            nums1[p] = nums2[p2]
            p2 += 1

    print(nums1)


# merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
# merge([1], 1, [], 0)
# merge([], 0, [], 0)

"""O(m+n): Time Complexity
O(m) : Space Complexity"""


def merge2(nums1, m, nums2, n):

    num1copy = nums1[:m]

    p1 = p2 = p = 0

    while p < (m + n):

        if p2 >= n or (p1 < m and num1copy[p1] < nums2[p2]):

            nums1[p] = num1copy[p1]
            p1 += 1

        else:

            nums1[p] = nums2[p2]
            p2 += 1

        p += 1

    print(nums1)


# merge2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# merge2([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
# merge2([1], 1, [], 0)
# merge2([], 0, [], 0)


"""O(m+n): Time Complexity
O(1) : Space Complexity"""


def merge3(nums1, m, nums2, n):

    p1 = m - 1
    p2 = n - 1

    for p in range(m + n - 1, -1, -1):

        if p2 < 0:

            break

        if p1 >= 0 and nums1[p1] > nums2[p2]:

            nums1[p] = nums1[p1]
            p1 -= 1

        else:

            nums1[p] = nums2[p2]
            p2 -= 1

    print(nums1)


merge3([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
merge3([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
merge3([1], 1, [], 0)
merge3([], 0, [], 0)
