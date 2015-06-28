#!/usr/lib/python
import pdb
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        #dynimic programming
        #f[i][j] = max(f[i-1][j-1], f[i-1][j] , f[i][j-1] + 1 ) + 1 if S[i]==T[j] else 0
        print S,T
        m = len(S)
        n = len(T)
        if m < n:
            return 0
        
        f = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if j > i:
                    continue
                if S[i-1] == T[j-1]:
                    if f[i-1][j] != 0:
                        #if f[i-1][j-1] >= f[i-1][j]:
                        #    f[i][j] = f[i-1][j] + f[i-1][j-1]
                        #else:
                        #    print i ,j, f[i-1][j-1]
                        #    f[i][j] = f[i-1][j] + 1
                        if i==1 or j==1:
                            f[i][j] = f[i-1][j] + 1
                        else:
                            f[i][j] = f[i-1][j] + f[i-1][j-1]
                    else:
                        if j ==1 or i == 1: 
                            f[i][j] = f[i-1][j-1] + 1
                        else:
                            f[i][j] = f[i-1][j-1]

                else:
                    f[i][j] = f[i-1][j]

        for x in f:
            print x
        return f[m][n]

if __name__ == "__main__":  
    s = Solution()
    print s.numDistinct("bbb","bb")
    print s.numDistinct("aabb","ab")
    print s.numDistinct("aabb","abb")
    print s.numDistinct("aabb","abb")
    print s.numDistinct("rabbbit","rabit")

    print s.numDistinct("aacaacca", "ca")
    print s.numDistinct("aaaaaaaaaaaaa", "aa")
    
