#!/usr/lib/python
import pdb
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num) <= 3:
            return sum(num)
        numsort = sorted(num)
        closest = None
        for i in range(len(numsort)):
            num1 = numsort[i]
            subtarget = target - num1
            high = len(numsort) - 1
            low = i + 1
            flag = 0 
            presumlh = None
            pdb.set_trace()
            while low < high:
                sumlh = numsort[low] + numsort[high]
                if presumlh is None:
                    presumlh = sumlh
                elif abs(presumlh - subtarget) <= abs(sumlh - subtarget):
                    break
                
                if sumlh > subtarget:
                    high -= 1
                elif sumlh < subtarget:
                    low += 1
                elif sumlh == subtarget:
                    return sumlh + num1
                presumlh = sumlh
            
            if closest is None:
                closest = presumlh + num1
            elif presumlh and  abs(presumlh + num1 - target) < \
                abs(closest - target):
                    closest = presumlh + num1
        return closest

if __name__ == "__main__":
    s = Solution()
    print s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
                
