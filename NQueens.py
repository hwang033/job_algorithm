#!/usr/lib/python
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        #backtrackig method
        rst = []
        self.NQueens(n, [], [], rst, [])
        return rst
    
    def NQueens(self, n, cols, diag, rst, subrst):
        
        if len(subrst) == n:
            rst.append(subrst)
            return 
        if len(subrst) > n:
            return 
        
        for i in range(n):
            if (i not in cols) and (i not in diag):
                line = "%sQ%s" %('.'*(i), '.'*(n-i-1))
                subrst.append(line)
                cols.append(i)
                diag.append(i)
                self.NQueens(n, cols[:], [x-1 for x in diag if x-1 >= 0], rst, subrst[:])
                diag.pop()
                cols.pop()
                subrst.pop()
if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(2)
    print s.solveNQueens(3)
    print s.solveNQueens(4)

