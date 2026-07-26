class Solution:
    def subsetXORSum(self, nums):
        n = len(nums)
        ans = 0

        # Generate all subsets
        for mask in range(1 << n):

            xor = 0

            # Build the subset using bits
            for i in range(n):
                if mask & (1 << i):
                    xor ^= nums[i]

            ans += xor

        return ans