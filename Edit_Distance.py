#!/usr/lib/python
import pdb
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        #dynamic program
        # f[i][j] = min(f[i-1][j-1] + 1 if words1[i] == words2[j] else 0, f[i-1][j] + 1, f[i][j-1] + 1)
        m = len(word1)
        n = len(word2)
        
        f = [[ 0 for j in range(n + 1)] for i in range(m + 1)]
        
        f[0] = [j for j in range(n + 1)]
        
        for i in range(m+1):
            f[i][0] = i
        
        for i in range(1, m+1):
            for j in range(1, n + 1):
                pdb.set_trace() 
                f[i][j] = min(f[i-1][j-1] + 0 if word1[i-1] == word2[j-1] else 1, f[i-1][j] + 1, f[i][j-1] + 1)
                
        return f[m][n]

if __name__ == "__main__":
    s = Solution()
    print s.minDistance("ab", "bc")
