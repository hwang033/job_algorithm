#!/usr/lib/python/
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        
        j = 0
        i = 0
        while i < m + j:
            if j >= n:
                break
            if A[i] >= B[j]:
                A.insert(i, B[j])
                j += 1
            else:
                i += 1
            
        while j < n:
            A.append(B[j])
            j += 1


if __name__ == "__main__":

    s = Solution()
    a = []
    b = [1]
    s.merge(a,0,b,1)
    #a = [1,4,5]
    #b = [0,2,6,7]
    #s.merge(a,3,b,4)
    print a      
