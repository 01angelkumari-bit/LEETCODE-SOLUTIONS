from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count=Counter(s1)  #dictionary of letters with thier freq is made
        window=Counter()  #empty dictionary {} created named window
        left=0
        if len(s1)>len(s2):
            return False
        for right in range(len(s2)):
            window[s2[right]]+=1
            if right-left+1 > len(s1):
                window[s2[left]]-=1   # dictionary se freq hta diye,eg a:1-->a:0
                if window[s2[left]]==0:
                    del window[s2[left]]
                left+=1
            if window==s1_count:
                return True
        return False 
