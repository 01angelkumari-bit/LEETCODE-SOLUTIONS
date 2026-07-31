class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for ch in s:
            if ch=="(":
                stack.append(ch)
            else:#  ) aagya
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(ch) #to store the ) that do not have the pair with (, hence append that also to calculate
        return len(stack)