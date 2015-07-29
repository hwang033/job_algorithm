class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        
        if x == 1.0 or n == 0:
            return 1.0
            
        if x == -1.0:
            if n % 2 == 0:
                return 1.0
            else:
                return -1.0

        rst = 1.0
        num = abs(n)

        for i in xrange(num):
            rst *= x
            if 0 < rst < 2.2250738585072014e-308:
                return 0.0
            if -2.2250738585072014e-308 < rst < 0:
                return 0.0
                
        if n < 0:
            return 1/rst
        

        return rst

if __name__ == "__main__":
    s = Solution()
    #print s.pow(-1.00000, -2147483648)
    print s.pow(-0.99999, 933520)
