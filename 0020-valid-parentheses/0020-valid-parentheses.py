class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opening_bracket=set(["{","[","("])
        brackets_map={ "}":"{",")":"(","]":"[" }
        for x in s:
            if x in opening_bracket:
                stack.append(x)
            elif x in brackets_map and stack and stack[-1]==brackets_map[x]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True