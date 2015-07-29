import pdb
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        
        a_l = [int(x) for x in a]
        b_l = [int(x) for x in b]
        
        rst = ""
        carry = 0
        
        i = len(a_l) - 1
        j = len(b_l) - 1
        
        while i >= 0 and j >= 0:
            subrst = a_l[i] + b_l[j] + carry
            if subrst > 1:
                carry = 1
                subrst -= 2
            else:
                carry = 0
                
            rst = str(subrst) + rst
            i -= 1
            j -= 1
        pdb.set_trace()
        while i > 0:
            
            subrst = a_l[i] + carry
            if subrst > 1:
                carry = 1
                subrst -= 2
            else:
                carry = 0
                
            rst = str(subrst) + rst
            i -= 1
            
        while j > 0:
            
            subrst = b_l[j] + carry
            if subrst > 1:
                carry = 1
                subrst -= 2
            else:
                carry = 0
                
            rst = str(subrst) + rst
            j -= 1
        
        if carry != 0:
            rst = str(carry) + rst
        
        return rst

if __name__ == "__main__":
    s = Solution()
    print s.addBinary('11', '1')
