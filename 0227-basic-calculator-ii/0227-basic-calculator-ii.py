class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        sign="+"
        s+="+"  #add dummy sight of add to check prev sign
        num=0
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch==" ":
                continue
            else:
                if sign=="+":
                    stack.append(num)
                if sign=="-":
                    stack.append(-num)
                if sign=="*":
                    a=stack.pop()*num
                    stack.append(a)
                if sign=="/":
                    a=int(stack.pop()/num)
                    stack.append(a)
                sign=ch
                num=0
        return sum(stack)
                


