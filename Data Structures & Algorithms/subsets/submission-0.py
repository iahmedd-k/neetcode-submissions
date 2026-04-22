class Solution:
    def subsets(self, nums):

        all_sets = []
        current = []

        def dfs(index):

            # every state is a valid subset
            all_sets.append(current.copy())

            for i in range(index, len(nums)):

                # choose
                current.append(nums[i])

                # explore
                dfs(i + 1)

                # un-choose (backtrack)
                current.pop()

        dfs(0)
        return all_sets