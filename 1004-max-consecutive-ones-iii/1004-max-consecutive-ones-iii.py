class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        number_of_zeros=0
        n=len(nums)
        left=0
        ans=0
        
        for right in range(n):
            if(nums[right]==0):
                number_of_zeros+=1

                while(number_of_zeros>k):
                    if(nums[left]==0):
                        number_of_zeros-=1
                    left+=1
            
            ans=max(ans,right-left+1)
        return ans