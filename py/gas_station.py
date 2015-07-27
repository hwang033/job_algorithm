#!/usr/lib/python/
import pdb
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        
        length = len(gas)

        i = 0    
            
        while i < length:
            pdb.set_trace()
            if gas[i] < cost[i]:
                i += 1
                continue
            prev = 0
            flag = 1
            for j in range(i, length + i):
                prev += gas[j%length] - cost[j%length]
                if prev < 0:
                    i = j%length
                    flag = 0
                    break
            i = j%length + 1
            if flag:
                return i
        return -1  

if __name__ == "__main__":
    s = Solution()
    print s.canCompleteCircuit([2,4],[3,4]) 
