#!/usr/lib/python 
class Solution:
    # @return an integers
    def numTrees(self, n):
        
        return self.findnumTrees( range(1, n+1))
    
    def findnumTrees(self, data):
        
        if data == [] or len(data) is 1:
            return 1

        rst = 0 
        for idx in xrange(len(data)):
            lnum = self.findnumTrees(data[:idx])
            rnum = self.findnumTrees(data[idx+1:])
            rst += lnum*rnum

        return rst


if __name__ == "__main__":
    s = Solution()
    print s.numTrees(3)
