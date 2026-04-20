class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Step 1: two pointers
        left = 0
        right = len(numbers) - 1

        # Step 2: move until they meet
        while left < right:

            # current sum
            total = numbers[left] + numbers[right]

            # Step 3: if we found the answer
            if total == target:
                # return 1-indexed positions
                return [left + 1, right + 1]

            # Step 4: if sum is too small → move left right
            elif total < target:
                left += 1

            # Step 5: if sum is too big → move right left
            else:
                right -= 1