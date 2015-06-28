import pdb
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # if s[i] == s[j] and f[i+1][j-1] == 1:
        #   f[i][j] = 1
        # mincut[i] = min(mincut[i-k] + (1 if f[i-k][i] == 1 else k) )
        f = [[0 for j in range(len(s)) ] for i in range(len(s))]
        mincut = [0 for i in range(len(s))]
        mincut[0] = 0
        
        for i in range(len(s)):
            f[i][i] = 1
        
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and ( j-i == 1 or f[i+1][j-1] == 1):
                    f[i][j] = 1
        print f 

        for i in range(1, len(s)):
            minval = ( 0 if f[0][i] == 1 else i)
            if minval != 0:
                for k in range(1, i+1 ):
                    val = mincut[i-k] + (1 if f[i-k+1][i] == 1 else k)
                    
                    minval = (val if val < minval else minval)
            mincut[i] = minval

        print mincut       
        return mincut[-1]

if __name__ == "__main__":
    s = Solution()
    input = ["bb","aaabaa","abb","abcde"]
    for x in input: 
        print x
        print s.minCut(x)
