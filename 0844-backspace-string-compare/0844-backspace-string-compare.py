class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(a:str):
            stack=[]
            for ch in a:
                if ch!="#":
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return "".join(stack)
        if build(s)==build(t):
            return True
        else :
            return False
