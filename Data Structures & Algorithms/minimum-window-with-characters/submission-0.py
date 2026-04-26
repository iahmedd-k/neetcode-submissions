class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        need = len(tCount)
        have = 0

        window = {}
        result = ""
        resultLen = float('inf')

        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in tCount and window[c] == tCount[c]:
                have += 1

            while have == need:
                # update result
                if (right - left + 1) < resultLen:
                    resultLen = right - left + 1
                    result = s[left:right + 1]

                # shrink window
                window[s[left]] -= 1
                if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1

                left += 1

        return result