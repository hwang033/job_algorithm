#!/usr/lib/python
import pdb
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        rst = []
        slen = len(s)
        self.getpartition(rst, [], s, slen)
        
        return rst[1] - 1
        
    def getpartition(self, rst, subrst, s, slen):
        if len(rst):
            if len(subrst) >= rst[1]:
                #print len(subrst) 
                return 
        
        length = 0
        for x in subrst:
            length += len(x)
        
        if length == slen:
            if not rst:
                rst.append(subrst)
                rst.append(len(subrst))
            else:
                if len(subrst) < rst[1]:
                    rst[0] = subrst
                    rst[1] = len(subrst)
            print rst
            return 

        if length > slen or not s:
            return 
        
        for i in range(len(s), -1, -1):

            substr = s[:i]
            if substr and self.isPalindrome(substr):
                subrst.append(substr)
                if len(rst):
                    if len(subrst) < rst[1]:
                        #print len(subrst) 
                        self.getpartition(rst,subrst[:], s[i:], slen)
                else:
                    self.getpartition(rst,subrst[:], s[i:], slen)

                subrst.pop()
                
    def isPalindrome(self, substr):        
        
        high = len(substr)-1
        low = 0
        while low <= high:
            if substr[low] == substr[high]:
                low += 1
                high -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    #print s.minCut("aaabaa")
    print s.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")

