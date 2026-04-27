from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # frequency map of s1
        s1_count = {}
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        # sliding window on s2
        s2_count = {}
        left = 0

        for right in range(len(s2)):
            # add current character to window
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1

            # shrink window if size exceeds s1
            if right - left + 1 > len(s1):
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]
                left += 1

            # compare frequency maps
            if s2_count == s1_count:
                return True

        return False