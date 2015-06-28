#!/usr/lib/python

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        
        sl = s.strip().lower()
        high = len(sl)-1
        low = 0
        while low<=high:
            
            while not sl[low].isalpha() and not sl[low].isalnum():
                low += 1
                if low > high:
                    return True
            while not sl[high].isalpha() and not sl[high].isalnum():
                high -= 1

            print low, high

            if sl[low] == sl[high]:
                low += 1
                high -=1
            else:
                return False
        
        return True

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome("1a2")
