class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(left,right):
            mid=(left+right)//2
            if left>right:
                return -1
            if nums[mid]>target:
                return binary(left,mid-1)
            elif nums[mid]==target:
                return mid
            else:
                return binary(mid+1,right)
        return binary(0,len(nums)-1)
                