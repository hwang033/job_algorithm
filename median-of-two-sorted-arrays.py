import pdb
class Solution:
    # @return a float
    def findMedianSortedArrays(self, m, n, k=None):
        if k==None:
            length_sum = len(m) + len(n)
            if length_sum%2 == 0:
                n1 = self.findMedianSortedArrays(m, n, k = length_sum/2)
                #print n1
                n2 = self.findMedianSortedArrays(m, n, k = length_sum/2 + 1)
                #print n2
                return (n1 + n2)*1.0/2
            else:
                k = length_sum/2 + 1
        print m , n , k, (k)/2-1, k/2#,  m[k/2-1], n[k/2-1] 
        if not n:
            return m[k-1]
        elif not m:
            return n[k-1]
        
        if k == 1:
            return m[0] if m[0] < n[0] else n[0] 
      
        mid_m, mid_n = 0, 0
        if k%2 == 0:
            mid_m = mid_n = k/2 - 1 
        else:
            if len(n) > len(m):
                mid_m, mid_n = k/2 - 1, k/2 
            else:
                mid_m, mid_n = k/2, k/2 - 1

        if mid_m > len(m) - 1:
            if m[-1] <= n[mid_n]:
                return self.findMedianSortedArrays([], n[mid_n:k], k - mid_n - len(m))
            if m[-1] > n[mid_n]:
                 return self.findMedianSortedArrays(m, n[mid_n:k], k - mid_n)

        elif mid_n > len(n) - 1:
            if n[-1] <= m[mid_m]:
                
                return self.findMedianSortedArrays(m[mid_m: k], [], k - mid_m- len(n) )
            if n[-1] > m[mid_m]:
                 return self.findMedianSortedArrays(m[mid_m:k], n, k - mid_m)

        else:
            if m[mid_m] < n[mid_n]:
                print "m[mid_m] < n[mid_n]"
                next_k = ( k/2 if mid_m == mid_n else k - mid_m -1 ) 
                return self.findMedianSortedArrays(m[mid_m + 1: k], n[:mid_n + 1], next_k)
            if m[mid_m] > n[mid_n]:
                print "m[mid_m] > n[mid_n]"
                next_k = ( k/2 if mid_m == mid_n else k - mid_n - 1) 
                return self.findMedianSortedArrays(m[:mid_m + 1], n[mid_n + 1:k], next_k)
            if m[mid_m] == n[mid_n]:
                #print "3"
                return m[mid_m]
    
if __name__ == "__main__":
    s = Solution()
    print s.findMedianSortedArrays([1,2], [1,2,3])
    print s.findMedianSortedArrays([1,2], [3,4])
    print s.findMedianSortedArrays([1,3,4], [2])
    print s.findMedianSortedArrays([2,3,4], [1])
    print s.findMedianSortedArrays([1,1,3,3], [1,1,3,3])
    print s.findMedianSortedArrays([1,3], [2,4])
    print s.findMedianSortedArrays([1], [2,3,4])
    print s.findMedianSortedArrays([4,5], [2,3])
    print s.findMedianSortedArrays([], [1,2,3,4,5])
    print s.findMedianSortedArrays([100000], [100001])
