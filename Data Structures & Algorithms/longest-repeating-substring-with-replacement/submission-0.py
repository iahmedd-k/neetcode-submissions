class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0      # highest freq of any char in current window
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # window size - most frequent char = replacements needed
            window_size = right - left + 1
            if window_size - max_freq > k:
                # shrink window
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result