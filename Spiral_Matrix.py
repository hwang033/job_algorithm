#!/usr/lib/python/

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        #recursive method
        rst = []
        self.spiralOr(rst, matrix)
        return rst
    
    def spiralOr(self, rst, matrix):
        
        if not matrix:
            return 
        submatrix = []
        
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return 
        
        for x in matrix[0]:
            #add first line
            rst.append(x)
        print rst    
        for i in range(1, m):
            #add last column
            rst.append(matrix[i][n-1])
        print rst    

        if m-1 != 0: 
            for j in range(n-2, -1, -1):
                #add last row
                rst.append(matrix[m-1][j])
            print rst    
        
        for k in range(m-2, 0, -1):
            #add first column
            rst.append(matrix[k][0])
        print rst    
        
        submatrix = [[matrix[i][j] for j in xrange(1, n-1)] for i in xrange(1, m-1)]
        self.spiralOr(rst, submatrix)

if __name__ == "__main__":
    
    s = Solution()
    print s.spiralOrder([[2,3]])
