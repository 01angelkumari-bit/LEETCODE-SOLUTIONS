class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left <right:
            if s[left]!=s[right]:
                skipL=s[left+1:right+1]  #r+1 bcz, r+1th letter is excluded
                skipR=s[left:right]    #right element is excluded(considered deleted)
                return skipL==skipL[::-1] or skipR==skipR[::-1] 
            else:
                left+=1
                right-=1
        return True