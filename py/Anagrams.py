class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        rst = set()
        d = {}
        for s in strs:
            sum_hash = sum([hash(x) for x in s])
          
            if d.has_key(sum_hash):
                rst.add(d[sum_hash])
                rst.add(s)
            else:
                d[sum_hash] = s
                
        return list(rst)
if __name__ == "__main__":
    s = Solution()
    print s.anagrams(["", "", "ac", "ca", "ac", "bd", "bc"])
