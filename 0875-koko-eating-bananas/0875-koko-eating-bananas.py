class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        answer=right
        while left <= right :
            hour=0
            mid=(left+right)//2
            for pile in piles:
                hour+=(pile+mid-1)//mid

            if hour<=h:   #agr calculated hour is less or same than given hour        
                answer=mid   #store in answer
                right=mid-1     #look for more smaller in left side
            else:
                left=mid+1   #find in right side
        return answer
