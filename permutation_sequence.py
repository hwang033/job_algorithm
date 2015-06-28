import pdb
class Solution:

    # @return a string
    def getPermutation(self, n, k):
        per = 1
        i = 1

        while i < n:
            per *= (i + 1)
            i += 1
        pdb.set_trace() 
        return self.helper(per, k, range(1, n+1))
    
    def helper(self, per, k, l):
        if not l:
            return ""
        
        per = per/len(l)
        
        div, mod = divmod(k, per)
        print k, per, div, mod
        
        num = 0
        if mod == 0 and div != 0:
            num = l.pop(div-1)
            mod = per
        else:
            num = l.pop(div)

        print num    

        return str(num) + self.helper(per, mod, l)
        

    '''
    def getPermutation(self, n, k):

        n_1_fac = 1

        for i in range(1, n):

            n_1_fac *= i

        return self.helper( n_1_fac, range(1, n+1), k)

    def helper(self, n_1_fac, n_list, k):

        
        n = len(n_list)

        if n == 1:

            return str(n_list[0])

        if n == 0:

            return ""

        rst = ""

        idx = k/(n_1_fac) - 1 if k%(n_1_fac) == 0 else k/(n_1_fac)

        #print n_1_fac, n_list, k, idx

        rst += str(n_list[idx]) + self.helper(n_1_fac/(n-1), n_list[:idx] + n_list[idx+1:], k - idx*n_1_fac)

        #print n_1_fac, n_list, k, idx, "rst:",rst
        return rst
    '''

if __name__ == "__main__":
    s = Solution()
    #print s.getPermutation(3, 2)
    #print s.getPermutation(4, 1)
    #print s.getPermutation(4, 2)
    print s.getPermutation(4, 3)
    #print s.getPermutation(4, 4)
    #print s.getPermutation(4, 5)
    #print s.getPermutation(4, 6)
        
