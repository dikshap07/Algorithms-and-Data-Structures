def maxArea(self, height):

    l, r, max_area = 0, len(height) - 1, 0

    while l < r:

        width = r - l
        print("l", l)
        print("r", r)
        curr_area = min(height[l], height[r]) * width

        max_area = max(curr_area, max_area)

        if height[l] < height[r]:

            l += 1

        else:
            r -= 1

    return max_area
