class Solution:
   
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def path(i,j):
          
            if i>=m or j>=n: #base case for outside matrix
                return 0
            if i==m-1 and j==n-1:#for one vallid path
                return 1
            right=path(i,j+1)
            down=path(i+1,j)
            total=right+down
            return total
        return path(0,0)


