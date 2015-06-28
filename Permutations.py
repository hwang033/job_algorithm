#!/usr/lib/python/

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        #backtrack
        rst = []
        self.permutebt(rst, len(num), [], num)
        return rst
        
    def permutebt(self, rst, n, subrst, numl):
        
        if len(subrst) == n:
            rst.append(subrst)
            
        for idx in xrange(len(numl)):
            x = numl[idx]
            subrst.append(x)
            self.permutebt(rst, n, subrst[:], numl[:idx] + numl[idx+1:])
            subrst.pop()    
        
if __name__ == "__main__":
    
    s = Solution()
    print s.permute([1])
