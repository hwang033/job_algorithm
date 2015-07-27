import pdb
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        #f[i][j] = f[i][j-1] + f[j-1][j] -1
        if not s or s[0] == "0":
            return 0
        if len(s) == 1: 
            return 1

        s_list = [int(x) for x in s]
        f = [0 for j in xrange(len(s))]
        decod = [] 

        for i in xrange(len(s) - 1):
            j = i+1
            if (s_list[i]*10 + s_list[j]) <= 26 and s_list[i] != 0 and s_list[j] !=0:
                decod.append(2)
            elif (s_list[i]*10 + s_list[j]) > 26 and s_list[j] == 0:
                decod.append(0)
            elif s_list[i] == 0:
                decod.append(0)
            else:
                decod.append(1)

        if s_list[-1] == 0 and len(s_list) > 1:
            decod.append(0)

        if s_list[-1] != 0 and len(s_list) > 1:
            decod.append(1)

        prev = decod[0]
        for i in xrange(1, len(decod)):
            if decod[i] == prev and prev == 0:
                return 0
            prev = decod[i]

        f[0] = 1 
        for i in xrange(1, len(s_list)):
            if f[i-1] > f[i-2] and i > 1:
                if decod[i] != 0:
                    f[i] = f[i-2]*decod[i-1] + (f[i-1] - f[i-2]) 
                else:
                    f[i] = f[i-2]
            else:
                if decod[i-1] == 0:
                    if decod[i] != 0: 
                        f[i] = f[i-1] 
                    else:
                        return 0 
                else:
                    if decod[i] == 0 and i > 1 and decod[i-2] != 0:
                        f[i] = f[i-2] 
                    else:
                        f[i] = f[i-1] * decod[i-1]
         
        print s
        print decod
        print f
        return f[-1]

        
if __name__ == "__main__":
    s = Solution()
    s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
    print s.numDecodings("1212")
    print s.numDecodings("121212")
    print s.numDecodings("230")
    print s.numDecodings("110")
    print s.numDecodings("100")
    #print s.numDecodings("101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010")
    print s.numDecodings("101010")
    print s.numDecodings("1012")
    print s.numDecodings("126421")