class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        #using binary search method
        
        high = len(A) - 1
        low = 0
        
        
        while low <= high:
            mid = (low + high)/2
            if A[mid] == target:
                return mid
            
            if A[high] <= A[low]:
                if target> A[mid]:
                    if target > A[high]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if target > A[high]:
                        high = mid - 1
                    else:
                        low = mid + 1
            else:
                if target> A[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
 
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.search([4,5,6,7,8,1,2,3], 8)
