#!/usr/lib/python
import pdb
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        #using backtracking method
        rst = []
        self.getsubsets(S, rst, [])
        return rst
    
    def getsubsets(self, S, rst, subrst):
        pdb.set_trace() 
        rst.append(subrst)
        if not S:
            return 
        
        for i in range(len(S)):
            subrst.append(S[i])
            self.getsubsets(S[i+1:], rst, subrst[:])
            subrst.pop()

if __name__ == "__main__":
    s = Solution()
    print s.subsets([1,2,3])

 
