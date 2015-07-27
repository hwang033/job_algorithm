class Solution:
    # @return a boolean
    def isMatch(self, s, p):

        p = [x for x in p]
        s = [x for x in s]
        star = None
        ss = i = j = 0
        
        
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
                continue

            if j < len(p) and p[j] == '*':
                star = j
                j += 1
                ss = i
                continue

            if star != None:
                j = star + 1
                ss += 1
                i = ss 
                continue
            
                    
            return False 
        
        while j < len(p) and p[j] == '*':
            j += 1
        
        return j == len(p)

                    
if __name__ == "__main__":                    

    s = Solution()
    input = [["aa", "*"], ["aaabbcbc", "a*bc"]]
    for i in input:
        print i
        print s.isMatch(i[0], i[1])
