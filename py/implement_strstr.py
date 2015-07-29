class Solution:

    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if haystack == "" and needle != "":
            return None

        if needle == "":
            return haystack

        t = self.kmp_table(needle)
        length = len(haystack)
        m = j = 0

        while m + j < len(haystack):

            if haystack[m+j] == needle[j]:
                if j == len(needle) - 1:
                    return haystack[m:]
                j += 1
            else:
                if t[j] > -1:
                    m = m + j - t[j]
                    j = t[j]
                else:
                    m = m + 1
                    j = 0
        
        return None
    
    def kmp_table(self, s):

        t = [0 for i in range(len(s))]
        t[0] = -1
        pos = 2
        cnd = 0

        while pos < len(s):
            if s[pos-1] == s[cnd]:
                cnd += 1
                t[pos] = cnd
                pos += 1
            else:
                if cnd > 0:
                    print cnd, pos, t
                    cnd = t[cnd]
                else:
                    t[pos] = 0
                    pos += 1
        return t
if __name__ == "__main__":
    s = Solution()
    #print s.kmp_table("ABCDABD")
    #print s.kmp_table("abcdeabcdabcd")
    print s.strStr("babbba", "bbb" )

