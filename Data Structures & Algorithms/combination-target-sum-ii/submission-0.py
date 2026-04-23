class Solution:
    def combinationSum2(self, nums, target):
        nums.sort()
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(list(current))
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):
                # 🔥 skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue

                current.append(nums[i])
                backtrack(i + 1, current, remaining - nums[i])  # ❗ i+1 (no reuse)
                current.pop()

        backtrack(0, [], target)
        return result