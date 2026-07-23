class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip=0
        while n>1:

            length=(1<<n)-1
            mid=1<<(n-1)
            if k==mid:
                return "1" if flip==0 else '0'
            if k>mid:
                k=length-k+1
                flip^=1
            n-=1
        return "0" if flip==0 else "1"
        