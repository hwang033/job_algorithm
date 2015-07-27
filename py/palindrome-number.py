class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        
        x1 = x
        y = 0
        
        while x1:
            div, mod = divmod(x1, 10)
            x1 = div
            y = y*10 + mod
        
        return x==y 

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome(1)
    print s.isPalindrome(121)
    print s.isPalindrome(21)
