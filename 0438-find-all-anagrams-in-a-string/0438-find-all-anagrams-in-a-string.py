class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        p_count=Counter(p) #{ letters od p and their freq is made to compare with anagram later }
        window=Counter() #{} empty window is creted to store window freq and get it compared
        left=0
        ans=[]
        for right in range(len(s)):
            window[s[right]]+=1
            if right-left+1 >len(p):
                window[s[left]]-=1     #dictionary k andr ka freq 0 thi, aur -1 hokr dictionary se hi htt jayegi
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
            if window==p_count:
                ans.append(left)
        return ans
