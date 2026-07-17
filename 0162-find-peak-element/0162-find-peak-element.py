class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # peak must be on the right side.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # so peak is at mid or on the left.
            else:
                right = mid
        # left == right
        return left