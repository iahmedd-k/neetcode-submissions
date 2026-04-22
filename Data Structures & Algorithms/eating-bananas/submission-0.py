import math

class Solution:
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)

        while left < right:

            mid = (left + right) // 2

            # calculate total hours needed at speed = mid
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                # mid works → try smaller k
                right = mid
            else:
                # too slow → increase k
                left = mid + 1

        return left