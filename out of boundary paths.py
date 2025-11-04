class Solution:
    def findPaths(self,m,n,maxMove,startRow,startColumn):

        def solve(i,j,maxMove):
            if maxMove<0:
                return 0
            if i<0 or i>=m or j<0 or j>=n:
                return 1
            
            a=solve(i-1,j,maxMove-1)
            b=solve(i+1,j,maxMove-1)
            c=solve(i,j-1,maxMove-1)
            d=solve(i,j+1,maxMove-1)
            
            return a+b+c+d
        
        return solve(startRow,startColumn,maxMove)%1000000007