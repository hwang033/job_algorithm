class Solution:
    # @return a list of integers
    def grayCode(self, n):
        
        rst = []
        for i in xrange(pow(2, n)):
            rst.append((i>>1)^i)
        return rst
            
        
            
if __name__ == "__main__":
    s = Solution()
    print s.grayCode(11)
