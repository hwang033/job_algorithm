class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        #using dynamic programming to solve this problem
        #f[i][j] denote isMatch up to word i, re j

        if not s:
            if (len(p) == 2 and p[1] == '*') or not p :
                return True
            return False
        elif not p:
            return False
        
        f = [ [ 0 for j in range(len(p)) ] for i in range(len(s)) ] 
        dup = 0
        for j in range(len(p)):        

            if s[0] == p[j] and dup == 0:
                f[0][j] = 1
                dup = 1

            elif p[j] == '.' and dup == 0:
                if j > 0 and p[j-1] != '*':
                    f[0][j] = 0
                    break
                dup = 1
                f[0][j] = 1

            elif p[j] == '.' and dup == 1:
                if p[j-1] == '*' and f[0][j-2] == 1:
                    f[0][j] = 1
                
            elif p[j] == '*' and j is not 0:
                if p[j-1] == '.' or f[0][j-1] == 1:
                    f[0][j] = 1
                elif f[0][j-2] == 1:
                    f[0][j] = 1
            

        print f 
        for i in range(1, len(s)):
            for j in range(len(p)):
                match = 0
                if p[j] == s[i]: 
                    match = 1
                elif p[j] == '*' and (s[i] == p[j-1] or p[j-1] == '.') :
                    match = 1
                elif p[j] == '.':
                    match = 1
                
                if match:
                    if j > 0 and f[i-1][j-1] == 1:
                        f[i][j] = 1
                    elif p[j] == '*' and (f[i-1][j] == 1 or f[i][j-1] == 1):
                        f[i][j] = 1
                else:
                    f[i][j] = 0
                    if p[j] == '*' and j > 1 and f[i][j-2] == 1:
                        f[i][j] = 1
            print f 

        if f[len(s)-1][len(p)-1] == 1:
            return True
        return False
                    
if __name__ == "__main__":                    

    s = Solution()
    #input = ["a", ".*..a*"]
    #input = ["a", "c*."]
    #input = ["aab", "b.*"]
    input = ["bbacbcabbbbbcacabb", "aa*c*b*a*.*a*a.*."]
    #input = ["aaa", "ab*ac*.*.a*"]
    #input = ["bbaa", "a..."]
    #input = ["a", ".*."]
    #input = ["aab", "c*a*b"]
    #input = ["aa", "a"]
    print input
    print s.isMatch(input[0], input[1])
