class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):

        self.reverse(s, 0, len(s) - 1)
        start = 0 

        for end in range(len(s)):
            if s[end] == " ":
                self.reverse(s, start, end - 1) 
                start = end + 1
            elif end == len(s) - 1:
                self.reverse(s, start, end) 
                start = end + 1
    
    def reverse(self, s, low, high):
        print low, high
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

if __name__ == "__main__":
    s = Solution()
    s.reverseWords(['a', ' ', 'b'])
    s.reverseWords(['h', 'i', '!'])
