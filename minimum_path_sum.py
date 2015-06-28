class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if not grid:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        
        f = [grid[0][0]]
        for i in range(1, n):
            f.append(grid[0][i] + f[i-1])        
  
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if j > 0:
                    f[j] = min(f[j-1], f[j]) + val
                elif i > 0:
                    f[j] = f[j] + val
            print f
        return f

if __name__ == "__main__":
    s = Solution()        
    s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
