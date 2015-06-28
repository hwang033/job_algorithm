#!/usr/bin/python
import pdb

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s or not dict:
            return False
        
        status = [0]
        for i in range(0, len(s)):
            for idx in status:
                word = s[idx:i+1]        
                if dict.has_key(word):
                    status.append(i+1)
                    break

        if status[-1] is len(s):
            return True
        return False

if __name__=="__main__":
    s ="leetcodex"
    dict = {'leet':1, 'code':1}
    sol = Solution()
    print sol.wordBreak(s, dict)
