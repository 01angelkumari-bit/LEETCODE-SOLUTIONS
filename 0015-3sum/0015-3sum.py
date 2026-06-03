class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-1):

            left=i+1
            right=len(nums)-1
            total=0
            if(i>0 and nums[i]==nums[i-1]):
                continue
            while(left<right):
                total=nums[i]+nums[right]+nums[left]
                if(total==0):
                    result=result+[[nums[i],nums[right],nums[left]]]
                    left+=1
                    right-=1
                    # skip duplicate left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # skip duplicate right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif (0>total):
                    left+=1
                else:
                    right-=1
        return result