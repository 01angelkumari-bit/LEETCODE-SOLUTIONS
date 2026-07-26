class Solution:
    def subsets(self, nums):
        n = len(nums)
        ans = []

        for mask in range(1 << n):      # 0 to 2^n - 1
            subset = []

            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])

            ans.append(subset)

        return ans