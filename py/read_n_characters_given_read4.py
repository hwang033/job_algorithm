# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        
        if len(buf) >= n:
            return n
        else:
            return len(buf)

if __name__ == "__main__":
    s = Solution()
    print s.read("", 1)
