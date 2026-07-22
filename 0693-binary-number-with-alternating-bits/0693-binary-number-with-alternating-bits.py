class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        while n > 1:

            last = n & 1
            second = (n >> 1) & 1

            if last == second:
                return False

            n >>= 1
        return True