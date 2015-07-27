#!/usr/lib/python
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A:
            return 1
        f = [-1 for i in range(len(A))]
        
        for x in A:
            if x <= len(A) and x > 0:
                f[x-1] = x
        print f 

        for idx in range(len(f)):
            print idx + 1, f[idx]
            if (idx + 1) != f[idx]:
                return idx + 1
        
        return f[idx] + 1
if __name__ == "__main__":
    s = Solution()
    print s.firstMissingPositive([1])
