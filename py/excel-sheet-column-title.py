class Solution:
    # @return a string
    def convertToTitle(self, num):
        
        rst = ""
        n1 = num
        div = 2
        
        while div > 0:
            div, mod = divmod(n1, 26)
            if mod != 0:
                rst = "%s%s" %(chr(mod - 1 + 65), rst)
            else:
                rst = "Z%s" %(rst)
                div -= 1
            n1 = div
            
        return rst

if __name__ == "__main__":
    s = Solution()
    print s.convertToTitle(26)
    print s.convertToTitle(703)
