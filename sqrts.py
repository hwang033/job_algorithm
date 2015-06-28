class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
    #binary search method
        low = 0
        high = x/2
        val = 0
        while low <= high:
            val = (low + high)/2 
            print val
            if val*val > x:
                high = val - 1
            elif val*val < x:
                low = val + 1
            else:
                return val
        
        return val if val*val < x else val-1

if __name__ == "__main__":
    s = Solution()
    #print s.sqrt(101)
    print s.sqrt(6)
    #print s.sqrt(1579205274)

