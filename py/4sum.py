class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        
        sorted_num = sorted(num)
        print sorted_num
        rst = [] 
        for i in range(len(sorted_num)-3):
            
            if i > 0 and sorted_num[i] == sorted_num[i-1]: 
                continue
                
            j = i + 1
            while j < len(sorted_num) -2:
                if j > i + 1 and sorted_num[j] == sorted_num[j-1]: 
                    j += 1
                    continue
                remain_sum = target - (sorted_num[i] + sorted_num[j])
                low = j+1
                high = len(sorted_num) - 1

                print "#",[i, j, low, high]

                if remain_sum > (sorted_num[high] + sorted_num[high-1]) or \
                    remain_sum < (sorted_num[low] + sorted_num[low+1]):
                    j += 1
                    continue
                
                while low < high:
                    if sorted_num[low] + sorted_num[high] > remain_sum:
                        high -= 1
                    elif sorted_num[low] + sorted_num[high] < remain_sum:
                        low += 1
                    elif sorted_num[low] + sorted_num[high] == remain_sum:
                        print [sorted_num[i], sorted_num[j], sorted_num[low],\
                            sorted_num[high]]
                        print "#",[i, j, low, high]
                        rst.append([sorted_num[i], sorted_num[j], 
                                   sorted_num[low], sorted_num[high]]) 
                        
                        while sorted_num[high] == sorted_num[high-1]\
                            and high > low:
                            high -= 1
                        high -= 1
                        
                        while sorted_num[low] == sorted_num[low + 1] \
                            and low < high:
                            low += 1
                        low += 1
                j += 1
                
        return rst
if __name__ == "__main__":
    s = Solution()
    #print s.fourSum([-1,0,1,2,-1,-4], -1)
    print s.fourSum([-3,-2,-1,0,0,1,2,3], 0)
    print s.fourSum([-1,-5,-5,-3,2,5,0,4], -7 )
    print s.fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9 )
    print s.fourSum([0,0,0,0], 0)
