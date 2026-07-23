class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        ans = n & (n - 1)

        if ans == 0:
            return True

        return False