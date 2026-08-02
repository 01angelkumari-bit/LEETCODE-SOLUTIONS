class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        remove=set()
        ans=[]
        for i,ch in enumerate(s):
            if ch=="(":
                stack.append(i)
            if ch==")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        while stack:#stack is still not emoty ,means no ) come for (
            remove.add(stack.pop())
        for i,ch in enumerate(s):
            if i not in remove:
                ans.append(s[i])

        return "".join(ans)

