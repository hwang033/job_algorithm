class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        
        s_list = list(s)
        has_e = False
        has_dot = False
        
        for idx, x in enumerate(s_list):
            if not x.isdigit():
                if x == 'e' and not has_e and idx < len(s_list) - 1:
                    has_e = True
                    continue
                
                if x == '.' and not has_dot and idx < len(s_list) - 1:
                    has_dot = True
                    continue
                
                return False    
            
        return True

if __name__ == "__main__":
    s = Solution()
    print s.isNumber("e9")
