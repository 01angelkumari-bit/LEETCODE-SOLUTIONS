class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left=1
        right=position[-1]-position[0]
        answer=0
        while left<=right:
            mid=(left+right)//2
            ball=1
            last_position=position[0]   #ball first placed at index 1
            for i in range(1,len(position)):
                if position[i]-last_position>=mid  :
                    ball+=1
                    last_position=position[i]
            if ball>=m:
                answer=mid
                left=mid+1
            else:
                right=mid-1
        return answer
                

