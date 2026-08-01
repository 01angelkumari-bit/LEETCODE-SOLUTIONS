class CustomStack:

    def __init__(self, maxsize: int):
        self.stack=[]
        self.maxsize=maxsize  #maxsize of stack,therfore overflow condition is given 

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxsize:
            self.stack.append(x)
        else:
            return False
    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        limit=min(len(self.stack),k)
        for i in range(limit):
            self.stack[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)