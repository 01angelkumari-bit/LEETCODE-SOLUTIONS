class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def money(i):
            if i>=len(nums):
                return 0
            takemoney=nums[i]+money(i+2)
            leavemoney=money(i+1)
            return max(takemoney,leavemoney)
        return money(0)