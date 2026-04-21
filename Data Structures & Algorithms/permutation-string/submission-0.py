class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Edge case
        if len(s1) > len(s2):
            return False

        count_s1 = {}
        count_window = {}

        # Build frequency of s1
        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1

        # First window
        for i in range(len(s1)):
            count_window[s2[i]] = count_window.get(s2[i], 0) + 1

        if count_s1 == count_window:
            return True

        # Sliding window
        for right in range(len(s1), len(s2)):
            # Add right char
            add = s2[right]
            count_window[add] = count_window.get(add, 0) + 1

            # Remove left char
            left = right - len(s1)
            remove = s2[left]
            count_window[remove] -= 1

            if count_window[remove] == 0:
                del count_window[remove]

            if count_s1 == count_window:
                return True

        return False