class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        def expand(left, right):
            nonlocal count # kyuki count function k bhe assigned and usme increment krna hoga

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)      # Odd palindrome
            expand(i, i + 1)  # Even palindrome

        return count