import pdb
class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        col = set([])
        ldiag = set([])
        rdiag = set([])
        return self.helper(n, 0, col, ldiag, rdiag)
        
    def helper(self, n, cur, col, ldiag, rdiag):
        if cur == n:
            return 1
            
        rst = 0
        for j in range(n):
            print j, col, ldiag, rdiag
            if (j not in col) and (j not in ldiag) and (j not in rdiag):
                col.add(j)
                ldiag.add(j)
                rdiag.add(j)
                rst += self.helper(n, cur+1, set([cl for cl in col]), set([ld - 1 for ld in ldiag if ld > 0 ]), set([rd + 1 for rd in rdiag if rd < n]))
                col.remove(j)
                ldiag.remove(j)
                rdiag.remove(j)

        return rst
                

if __name__ == "__main__":
    s = Solution()
    print s.totalNQueens(5)
