#!/usr/lib/python/
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        #binary search column first
        #binary search row second
        
        crst = self.binary_search_interval(matrix, target)
        print crst
        return self.binary_search(crst, target)

        
    def binary_search_interval(self, matrix, target):
        
        if target < matrix[0][0]:
            return []
            
        for i in xrange(len(matrix)-1):
            
            print  matrix[-1][0]        
            if target >= matrix[i][0] and target < matrix[i+1][0]:
                return matrix[i]
        if target >= matrix[-1][0]:
            return matrix[-1]
    
    def binary_search(self, slist, target):
        if not slist:
            return False
        high = len(slist) - 1
        low = 0

        while high >= low:
            mid = (low + high)/2
            if slist[mid] == target:
                return True
            if slist[mid] > target:
                high = mid -1
            if slist[mid] < target:
                low = mid+1
        return False       
        
if __name__ == "__main__":

    s = Solution()
    print s.searchMatrix([[1],[3]], 3)

