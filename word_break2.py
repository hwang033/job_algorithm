#!/usr/bin/python
import pdb
from copy import deepcopy

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreak(self, s, dict):
        if (not s) or (not dict) or ( not self.wordBreakable(s, dict) ):
            return [] 
        words = [set([]) for x in range(len(s)+1)]
        status = [0]
        for i in range(0, len(s)):
            for idx in status:
                word = s[idx:i+1]        
                if word in dict:
                    status.append(i+1)
                    words[i+1].add(word)

        if status[-1] is not len(s):
            return [] 

        output = []

        self.wordVisit(output, words, len(s), "")
        return output 

    def wordVisit(self, output, words, i, strrst):
        if i < 1 and strrst:
            output.append(strrst.strip())
            return

        wordslist = words[i]
        for w in wordslist:
            self.wordVisit(output,words, i-len(w), w + " " + strrst)

    def wordBreakable(self, s, dict):
        
        status = [0]
        for i in range(0, len(s)):
            stlen = len(status)
            for idx in xrange(0, stlen):
                word = s[status[idx]:i+1]
                if word in dict:
                    status.append(i+1)
                    break
                    
        if status[-1] is not len(s):
            return False
            
        return True
#
#        if not s or not dict:
#            return []
#
#        endset = set([0])
#        rst = [[0]]
#        rmidx = 0
#        output = [""]
#        flag = 0
#        Slen = len(s)
#        endsetlist = [0]
#
#        for i in range(0, Slen):
#
#            for idx in range(0, len(endset)):
#                endsetlist = list(endset)
#                word = s[endsetlist[idx]:i+1]
#                if word in dict:
#                    endset.add(i+1)
#
#                    if i+1 < Slen:
#                        rmidx = len(rst)
#                    elif i+1 is Slen and flag is 0:
#                        rmidx = len(rst)
#                        flag = 1
#
#                    for j in range(0, rmidx):
#                        if rst[j][-1] == endsetlist[idx]:
#                            temp = rst[j][:]
#                            temp.append(i+1)
#                            rst.append(temp)
#
#                            tempoutput = output[j]
#                            tempoutput += ' ' + word
#                            output.append(tempoutput)
#
#        if flag:
#            return [opt.strip() for opt in output[rmidx:]]
#
#
#
#        return []

if __name__=="__main__":
    #s ="aaaaaaaa"
    #dict = {'aaaa':1, 'aa':1,'a':1}
    #s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    #dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"] 
    #s = "a"
    #dict = ["a"]
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    sol = Solution()
    print sol.wordBreak(s, dict)
