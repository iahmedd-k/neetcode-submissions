class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Step 1: sort array
        nums.sort()
        res=[]
        # Step 2: fix one number
        for i in range(len(nums)):

            # skip duplicate fixed numbers
            if i > 0 and nums[i]==nums[i-1]:
                continue
            
            
            left = i + 1
            right = len(nums) - 1

            # Step 3: two pointers for remaining 2 numbers
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # skip duplicates for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1  # need bigger sum

                else:
                    right -= 1  # need smaller sum

        return res