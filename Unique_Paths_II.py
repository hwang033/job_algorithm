#!/usr/lib/python 
import pdb
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        #useing dynamic programming
        pdb.set_trace() 
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        f = [[0 for j in xrange(n)] for i in xrange(m)]
        
        if f[0][0] != 1:
            f[0][0] = 1
        
        
        for j in range(1, n):
            if f[0][j] == 1:
                f[0][j] = 0
            else: 
                f[0][j] = f[0][j-1]
                
        for i in range(1, m):
            if f[i][0] == 1:
                f[i][0] = 0
            else:
                f[i][0] = f[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if f[i][j] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]

if __name__ == "__main__":
    s = Solution()
    print s.uniquePathsWithObstacles([[1]]) 
