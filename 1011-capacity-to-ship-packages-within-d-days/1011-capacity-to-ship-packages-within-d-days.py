class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        answer=right
        while left <right:
            load=0
            day_needed=1
            mid=(left+right)//2
            for weight in weights:
                if load+weight > mid:
                    day_needed+=1
                    load=weight
                else:
                    load+=weight
            if day_needed<=days:
                right=mid
            else:
                left=mid+1
        return left

        

