class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        curr_max=max_sum=nums[0]
        for num in nums[1:]:   #kyuki circular hai isliye end nhi h
            curr_max=max(num,curr_max+num)
            max_sum=max(max_sum,curr_max)
        curr_min=min_sum=nums[0]
        for num in nums[1:]:   
            curr_min=min(num,curr_min+num)
            min_sum=min(min_sum,curr_min)
        if max_sum<0:    #for edge cases
            return max_sum
        return max(max_sum,total_sum-min_sum)


