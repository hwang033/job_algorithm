#!/usr/lib/python
import pdb
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        rst = []
        self.getcombinationSum(rst, target, sorted(candidates), [])
        return rst
        
    def getcombinationSum(self, rst, target, candidates, subrst):
        #backtracking
        if sum(subrst) == target:
            rst.append(subrst)
            return 
        if sum(subrst) > target:
            return   

        for idx in range(len(candidates)):
            subrst.append(candidates[idx])
            self.getcombinationSum(rst, target, candidates[idx:], subrst[:])
            subrst.pop()            

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([6,4,3,10,12], 28)
