import time
import pdb

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):

        d = {} 
        rst_l = [] 
        add_digit = 0
        k = 0
        if len(num1) < len(num2): 
            num1, num2 = num2, num1

        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]

        for i in range(len(num1) - 1, -1, -1):
            subrst = [] 
            if d.has_key(num1[i]):
                subrst = d[num1[i]]
            else:
                for j in range(len(num2) - 1, -1, -1):
                    digit_mul = int(num1[i])*int(num2[j]) + add_digit
                    add_digit, added = divmod(digit_mul, 10)
                    subrst.append(added) 

            while add_digit is not 0: 
                add_digit, added = divmod(add_digit, 10)
                subrst.append(added)  
            d[num1[i]] = subrst
            #print subrst
            rst_l.append((subrst[::-1] + [0 for x in range(k)]) if subrst[-1] is not 0 else [0])
            k += 1

        max_len = len(max(rst_l, key=lambda x: len(x)))
        zipped_list = zip(*[ [0 for xx in range(max_len - len(x))] + x  for x in rst_l])
        add_digit = 0
        rst = [] 
        for x in zipped_list[::-1]:
            sub_sum = sum(x) + add_digit
            add_digit, added = divmod(sub_sum, 10)
            rst.append(added)

        print add_digit 

        while add_digit is not 0: 
            add_digit, added = divmod(add_digit, 10)
            rst.append(added)  

        return ''.join([str(x) for x in rst[::-1]])


#    def _add_string(self, str1, str2):
#    def _add_string(self, str1, str2):
#
#        i = len(str1) - 1
#        j = len(str2) - 1
#        add_digit = 0
#        subrst = ""
#        while i >= 0 and j >= 0:
#            digit_mul = str( int(str1[i]) + int(str2[j]) + add_digit )
#            if len(digit_mul) > 1:
#                add_digit = int(digit_mul[0])
#                subrst += digit_mul[1]
#            else:
#                add_digit = 0
#                subrst += digit_mul
#            i -= 1
#            j -= 1
#
#        while i >= 0:
#            digit_mul = str( int(str1[i]) + add_digit )
#            if len(digit_mul) > 1:
#                add_digit = int(digit_mul[0])
#                subrst += digit_mul[1]
#            else:
#                add_digit = 0
#                subrst += digit_mul
#            i -= 1
#
#        while j >= 0:
#            digit_mul = str( int(str2[j]) + add_digit )
#            #print subrst, str1[j], digit_mul, j
#            if len(digit_mul) > 1:
#                add_digit = int(digit_mul[0])
#                subrst += digit_mul[1]
#            else:
#                add_digit = 0
#                subrst += digit_mul
#            j -= 1
#
#        if add_digit is not 0:
#            subrst += str(add_digit)
#
#        return subrst[::-1]

def main():            
    s = Solution()
    a = "123456789"
    b = "987654321"
    #b = '9200'
    #a = '786'
    print a, b
    t = time.time()
    #print s.multiply("9369162965141127216164882458728854782080715827760307787224298083754", "7204554941577564438")
    #print s.multiply("7204554941577564438","9369162965141127216164882458728854782080715827760307787224298083754")
    print s.multiply(a, b)
    print time.time() - t
    #print 9369162965141127216164882458728854782080715827760307787224298083754*7204554941577564438
    print int(a)*int(b)
      
    #print s._add_string('923','97')

if __name__ == "__main__":
    main()
