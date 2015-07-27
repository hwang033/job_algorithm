class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        #Using dynamic programming 
        
        if len(s3) != len(s1) + len(s2):
            return False
        
        if not s3:
            return True
            
        f = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        
        f[0][0] = 1
        
        #for i in range(len(s1)):
        #    idx_i = i + 1
        #    if s1[i] == s3[i] and f[idx_i-1][0] == 1:
        #        f[idx_i][0] = 1
        #
        #for j in range(len(s2)):
        #    idx_j = j + 1
        #    if s2[j] == s3[j] and f[0][idx_j-1] == 1:
        #        f[0][idx_j] = 1   
                    
                
        for i in range(-1, len(s1)):
            idx_i = i + 1
            for j in range(-1, len(s2)):
                idx_j = j + 1
                if i!= -1 and f[idx_i-1][idx_j] == 1 and s1[i] == s3[i+j+1]:
                    f[idx_i][idx_j] = 1
                if j!= -1 and f[idx_i][idx_j-1] == 1 and s2[j] == s3[i+j+1]:
                    f[idx_i][idx_j] = 1
                #print s1[i], s2[j], s3[i+j+1], i, j, i+j+1

        print f
        if f[-1][-1] == 1:
            return True

        return False

if __name__ == "__main__":
    s = Solution()
    p = [["aabd", "abdc", "aabdbadc"],["a", "b", "ab"],["aabcc", "dbbca", "aadbbcbcac"], ["aabcc", "dbbca", "aadbbbaccc"]]
    for x in p:
        print x
        print s.isInterleave(x[0], x[1], x[2])
    

