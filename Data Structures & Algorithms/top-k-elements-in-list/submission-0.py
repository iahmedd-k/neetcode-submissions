from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequencies
        freq = Counter(nums)

        # Step 2: Sort numbers by frequency (descending)
        sorted_nums = sorted(freq, key=lambda x: freq[x], reverse=True)

        # Step 3: Return top k elements
        return sorted_nums[:k]