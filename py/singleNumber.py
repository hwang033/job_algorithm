#!/usr/bin/python
#using Exclusive OR to solove this problem
#Bitwise operation
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        rst = 0
        for a in A:
            rst ^= a  
        return rst

