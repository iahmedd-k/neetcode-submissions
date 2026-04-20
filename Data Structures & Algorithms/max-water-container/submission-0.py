class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            # correct width
            width = right - left

            # limiting height
            h = min(heights[left], heights[right])

            # current area
            area = width * h

            # update answer
            max_water = max(max_water, area)

            # move the smaller height pointer
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water