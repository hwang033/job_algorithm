class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        #using dynamic programming to solve this problem
        #f[i][j] denote isMatch up to word i, re j
        # if p == '.' or p == s: if f[i-1][j-1] == 1
        # if p == '*': if f[i][j-1] == 1: f[i][j] == 1 elif f[i][j-2] == 1: f[i][j] = 1

        f = [ [ 0 for j in range(len(p) + 1) ] for i in range(len(s) + 1) ] 

        f[0][0] = 1
        for j in range(1, len(p) + 1):
            p_idx = j-1
            if p[p_idx] == '*' and f[0][j-2] == 1:
                f[0][j] = 1

        for i in range(1,len(s) + 1):
            s_idx = i - 1
            for j in range(1, len(p) + 1):
                p_idx = j - 1
                if (p[p_idx] == '.' or s[s_idx] == p[p_idx]) and f[i-1][j-1] == 1: 
                    f[i][j] = 1
                elif p[p_idx] == '*':
                    if f[i][j-1] == 1 or f[i][j-2] == 1:
                        f[i][j] = 1
                    elif s[s_idx] == p[p_idx-1] or p[p_idx-1] == '.':
                        f[i][j] = f[i-1][j] 
        print f             
        return f[-1][-1]

                    
if __name__ == "__main__":                    

    s = Solution()
    input = [["aaa", "ab*a"],["ab", ".*"],["aa","a*"],["a", ".*..a*"], ["a", "c*."], ["aab", "b.*"],\
            ["bbacbcabbbbbcacabb", "aa*c*b*a*.*a*a.*."],\
            ["aaa", "ab*ac*.*.a*"], ["bbaa", "a..."],\
            ["a", ".*."],  ["aab", "c*a*b"], ["aa", "a"]]
    for i in  input:
        print i
        print s.isMatch(i[0], i[1])
