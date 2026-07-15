class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_max=max_sum=nums[0]
         #same as maximum kadanes subarray sum
        for num in nums[1:]: 
            curr_max=max(num,curr_max+num)
            max_sum=max(max_sum,curr_max)
        #same as minimum kadanes subarray sum
        curr_min=min_sum=nums[0]
        for num in nums[1:]:   
            curr_min=min(num,curr_min+num)
            min_sum=min(min_sum,curr_min)
        # just return maximum abosolute value among above both
        return max(abs(max_sum),abs(min_sum))
    