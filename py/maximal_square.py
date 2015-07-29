class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, m):
        #if m[i][j] == 1
        #f[i][j] = min(f[i][j-1] + f[i-1][j-1] + f[i-1][j]) + 1
        if not m:
            return 0
        f = [[0 for j in range(len(m[0]) + 1)] for i in range(len(m) + 1)]
        max_val = 0
        for i in range(1, len(m) + 1):
            for j in range(1, len(m[0]) + 1):
                if m[i-1][j-1] == 1:
                    f[i][j] =  min(f[i][j-1], f[i-1][j-1], f[i-1][j]) + 1
                    max_val = max(f[i][j], max_val)
        
        return max_val**2
           

if __name__ == "__main__":
    s = Solution() 
    s.maximalSquare([[')
