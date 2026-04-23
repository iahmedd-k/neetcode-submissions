from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(list(current))
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, remaining - nums[i])  # reuse allowed
                current.pop()

        backtrack(0, [], target)
        return result