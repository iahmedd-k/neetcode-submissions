class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: If lengths differ, cannot be anagram
        if len(s) != len(t):
            return False

        # Step 2: frequency map
        freq = {}

        # Step 3: count characters in s
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 4: subtract using t
        for ch in t:
            # if character not found → invalid
            if ch not in freq:
                return False

            freq[ch] -= 1

            # if count goes negative → extra char in t
            if freq[ch] < 0:
                return False

        return True