#!/usr/lib/python 
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        rst = []
        self.findComb(rst, range(1, n+1), k, [])
        return rst
    
    def findComb(self, rst, data, k, subrst):
        
        if len(subrst) is k:
            rst.append(subrst[:])
            return 
        
        for idx in xrange(len(data)):
            subrst.append(data[idx])
            self.findComb(rst, data[idx+1:], k, subrst)
            subrst.pop()

if __name__ == "__main__":
    s = Solution()
    print s.combine(13,13)
