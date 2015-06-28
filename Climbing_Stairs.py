#!/usr/lib/python/

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        #use back track to slove this method
        
        return self.climbs(n, 0)
        
    def climbs(self, n, subrst):
        if subrst == n:
            return 1
        if subrst > n:
            return 0
            
        rst = 0
        
        rst += self.climbs(n, subrst + 1)
        rst += self.climbs(n, subrst + 2)
        return rst

if __name__ == "__main__":
    s = Solution()
    print s.climbStairs(4)
    print s.climbStairs(5)
    print s.climbStairs(6)
