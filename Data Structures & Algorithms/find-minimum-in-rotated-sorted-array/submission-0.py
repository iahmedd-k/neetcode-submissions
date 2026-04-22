class Solution:

    def findMin(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # minimum is on the RIGHT side
                left = mid + 1
            else:
                # minimum is at mid OR on the LEFT side
                right = mid

        return nums[left]