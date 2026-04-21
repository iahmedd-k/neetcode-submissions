class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in '([{':   # opening bracket
                stack.append(c)
            else:            # closing bracket
                if not stack:
                    return False

                if stack[-1] != matching[c]:
                    return False

                stack.pop()

        return len(stack) == 0