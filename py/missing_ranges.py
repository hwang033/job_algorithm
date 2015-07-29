#!/usr/lib/python
class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, A, lower, upper):
        
        A.insert(0, lower - 1)
        A.append(upper + 1)
        
        rst = []
        prev = A[0]
        print A 
        for x in A:
            if x - prev == 2:
                rst.append(str(x - 1))
            if x - prev > 2:
                rst.append("%d->%d" %(prev + 1, x - 1))
            prev = x
        
        return rst

if __name__ == "__main__":
    s = Solution()
    a = []
    print s.findMissingRanges(a, -3, -1)

