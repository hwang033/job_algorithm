class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):

        d = {}
        longest = 0
        cur_long = 0
        i = 0
        for idx, v in enumerate(s):
            if d.has_key(v):
                print '***', d
                longest = max(longest, cur_long)
                while i < d[v]:
                    d.pop(s[i])
                    i += 1
                print '---', d
                cur_long = len(d) - 1
                i += 1

            d[v] = idx
            cur_long += 1

        return max(longest, cur_long)
'''
        d = {}
        longest = 0
        cur_long = 0
        
        for idx, v in enumerate(s):
            if d.has_key(v):
                #remove elemnts before v
                longest = max(longest, cur_long)
                v_idx = d[v]
                del_l = []
                for k, val in d.iteritems():
                    if val <= v_idx:
                        del_l.append(k)
                for x in del_l:
                    d.pop(x)
                cur_long = len(d)
                
            d[v] = idx
            cur_long += 1        
        
        return max(longest, cur_long)
'''
'''
        if not s or len(s) == 1:
            return s
        
        s_l = [x for x in s]
        showed = {} 
        rst = []
        start = 0
        i = 0
        #print s 
        while i < len(s_l):
            cur = s_l[i]
            if showed.has_key(cur):
                #print s_l[start: i]
                rst = (s_l[start: i] if (i - start) > len(rst) else rst) 
                j = showed[cur]  
                start = j + 1
                while showed.has_key(j):
                    val =  showed[j] 
                    del showed[val]
                    del showed[j]
                    j -= 1

            showed[cur] = i
            showed[i] = cur 
            i += 1
            
        
        rst = (s_l[start: i + 1] if (i - start) > len(rst) else rst) 
        #print rst
        return len(rst)
'''
                
           
if __name__ == "__main__":
    s = Solution()

    print s.lengthOfLongestSubstring("abcabcbb")
    print s.lengthOfLongestSubstring("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco")
    print s.lengthOfLongestSubstring("bc")
