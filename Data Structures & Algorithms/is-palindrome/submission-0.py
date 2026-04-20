class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Step 1: Start two pointers
        # left starts from beginning, right starts from end
        left = 0
        right = len(s) - 1

        # Step 2: Keep checking until pointers meet in the middle
        while left < right:

            # Step 3: Skip characters from left that are NOT letters/numbers
            # Example: space, comma, colon, etc.
            while left < right and not s[left].isalnum():
                left += 1

            # Step 4: Skip characters from right that are NOT letters/numbers
            while left < right and not s[right].isalnum():
                right -= 1

            # Step 5: Compare characters (ignore uppercase vs lowercase)
            # Example: 'A' == 'a'
            if s[left].lower() != s[right].lower():
                return False  # mismatch → not a palindrome

            # Step 6: Move both pointers inward
            left += 1
            right -= 1

        # Step 7: If no mismatches found → it's a palindrome
        return True