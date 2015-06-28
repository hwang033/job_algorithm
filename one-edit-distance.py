import pdb
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isOneEditDistance(self, s, t):
        diff = 0
        if len(s) == len(t):
            i = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff += 1
            if diff == 1:
                return True
        elif abs(len(s)-len(t)) == 1:
            if s == "" or t == "":
                return True
            if len(s) > len(t):
                 if self.cal_diff(t, s) == 1:
                     return True
            else:
                 if self.cal_diff(s, t) == 1:
                     return True
        return False

    def cal_diff(self, s, t):
        
        i, j = 0, 0
        diff = 0
        pdb.set_trace()
        
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                print s[i], t[j]
                j += 1
                diff += 1
                continue
            i += 1
            j += 1

        return diff + len(t) - j
if __name__ == "__main__":
    s = Solution()            
    print s.isOneEditDistance("a", "ac")
    print s.isOneEditDistance("a", "ba")
