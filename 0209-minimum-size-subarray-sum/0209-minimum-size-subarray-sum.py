class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        min_value=float('inf')
        cur_sum=0
        for right in range(len(nums)):
            cur_sum+=nums[right]
            while(cur_sum>=target):
                min_value=min(min_value,right-left+1)
                cur_sum-=nums[left]
                left+=1
        if(min_value==float('inf')):   # given in question
            return 0
        else :
            return min_value
            
        