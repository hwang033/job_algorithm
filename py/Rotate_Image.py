#!/usr/lib/python/

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        
        dim = len(matrix)
        #transpose matrix
        for i in xrange(dim):
            for j in xrange(i, dim):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse each row
        for k in xrange(dim):
            low = 0
            high = dim-1
            while low < high:
                matrix[k][low], matrix[k][high] = matrix[k][high], matrix[k][low]
                low += 1
                high -= 1
            
        return matrix

if __name__ == "__main__":
    s = Solution()
    print s.rotate([[1,2],[3,4]] )
