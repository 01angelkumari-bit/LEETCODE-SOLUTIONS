class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        if hour <= len(dist) - 1:  #impposible, agr hour jda hoga total element in distance array,then wait time increases as each have to wait for next hour
            return -1
        left,right=1,10**7
        while left<right:
            mid=(left+right)//2
            time_taken=0
            for i in range(len(dist)-1):
                time_taken+=ceil(dist[i]/mid)  #mid is speed from range(1,10^7),exclude last element dur to no waiting time
            time_taken+=(dist[-1]/mid)  #no wait,no ceil
            if time_taken<=hour:
                right=mid
            else:
                left=mid+1
        return left
