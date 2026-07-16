class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :
            return ""
        else:
            ans=""
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]  #slicing(right excluded left+1 --->right-1)
        for i in range(len(s)):
            #even palindrome
            p1=expand(i,i+1)
            #odd palindrome
            p2=expand(i,i)

            if len(p1)>len(ans):
                ans=p1
            if len(p2)>len(ans):
                ans=p2
        return ans

