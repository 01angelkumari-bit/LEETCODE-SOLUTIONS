class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for ch in s:
            if ch=="(":
                stack.append(0)# making 0 , kyuki nested bracket m aasakte h
            else:
                value=stack.pop()
                if value==0:
                    current_score=1
                    stack[-1]+=current_score
                else:
                    current_score=2*value
                    stack[-1]+=current_score
        return stack[-1]