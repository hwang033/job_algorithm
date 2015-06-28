#!/usr/lib/python
import pdb
def findnumber(m, n, k):
    
    print m , n , k, (k+1)/2-1#,  m[k/2-1], n[k/2-1] 
    
    if not n:
        return m[k-1]
    elif not m:
        return n[k-1]
    
    if k == 1:
        return m[0] if m[0] < n[0] else n[0] 

    mid = (k+1)/2 - 1
    if mid > len(m) - 1:
        if m[-1] <= n[mid]:
            return findnumber([], n[mid:k], k - mid - len(m))
        if m[-1] > n[mid]:
             return findnumber(m, n[mid:k], k - mid)
    elif mid > len(n) - 1:
        if n[-1] <= m[mid]:
            return findnumber(m[mid: k], [], k-mid-len(n) )
        if n[-1] > m[mid]:
             return findnumber(m[mid:k], n, k-mid)
    else:
        if m[mid] < n[mid]:
            return findnumber(m[mid+1: k], n[:mid+1], (k)/2)
        if m[mid] > n[mid]:
             return findnumber(m[:mid+1], n[mid+1:k], (k)/2)
        if m[mid] == n[mid]:
            return m[mid]


if __name__ == "__main__":

    print findnumber([1,3], [2, 4], 2)
    print findnumber([1,3], [2, 4], 3)
    print findnumber([1,2], [3, 4], 2)
    print findnumber([1,2], [3, 4], 3)
    print findnumber([100000], [100001], 2)
    print findnumber([100000], [100001], 1)
    #print findnumber([8,7,6,5,4,3], [10,9], 2)
    print findnumber([1,2,4,6,7,8], [3,5,9,10], 2)
    print findnumber([1,2,4,6,7,8], [3,5,9,10], 3)
    print findnumber([1,2,4,6,7,8], [3,5,9,10], 4)
    print findnumber([1,2,4,6,7,8], [3,5,9,10], 5)
    print findnumber([1,2,4,6,7,8], [3,5,9,10], 6)
    print findnumber([1,2,4,6,7,8], [3,5,9,10], 7)
    print findnumber([1,2,2,2,8], [2,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 12)
    print findnumber([1,2,2,2,3,3,3,3,3,3,3,3], [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 13)
    #print findnumber([3,3,3,6,10], [3], 5)
