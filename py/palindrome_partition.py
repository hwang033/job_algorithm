#!/usr/lib/python
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        rst = []
        slen = len(s)
        self.getpartition(rst, [], s, slen)
        return rst
        
    def getpartition(self, rst, subrst, s, slen):
        
        length = 0
        
        print subrst
        for x in subrst:
            length += len(x)
        
        if length == slen:
            rst.append(subrst)
            return 
        
        if length > slen or not s:
            return 
        
        for i in range(0, len(s)):
            substr = s[:i+1]
            if substr and self.isPalindrome(substr):
                subrst.append(substr)
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
    print s.partition("a")
