from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)

        def backtrack(current):
            if len(current) == len(nums):
                result.append(list(current))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                current.append(nums[i])

                backtrack(current)

                current.pop()
                used[i] = False

        backtrack([])
        return result