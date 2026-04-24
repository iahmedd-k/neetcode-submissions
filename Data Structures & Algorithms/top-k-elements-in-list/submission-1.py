from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_counter= Counter(nums)

        sorted_list= sorted(freq_counter, key= lambda x:freq_counter[x], reverse=True)
        
        return sorted_list[:k]