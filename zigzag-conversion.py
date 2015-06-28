import pdb
class Solution:
    # @return a string
    def convert(self, s, n_rows):
        if not s or not n_rows:
            return ""

        if n_rows == 1:
            return s
        rst = []
        s_l = [x for x in s]
        base = 2*n_rows - 2

        for i in xrange(n_rows):

            j = i
            flag = 0
            x1 = i*2
            x2 = base - i*2
            if x1 == 0 and x2 == 0:
                rst.append(s_l[j])
                return ''.join(rst)

            while j < len(s_l):
                rst.append(s_l[j])
                if flag % 2 == 0:
                    if x2 != 0:
                        j += x2
                    else:
                        j += x1
                else:
                    if x1 != 0:
                        j += x1
                    else:
                        j += x2
                flag += 1

        return ''.join(rst)
                                
if __name__ == "__main__":
    s = Solution()
    #print s.convert("PAYPALISHIRING", 3)
    print s.convert("ABCDE", 4)
