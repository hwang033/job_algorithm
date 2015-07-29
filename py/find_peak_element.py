import pdb
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):

        if not num:
            return 
        if len(num) == 1:
            return 0

        
        low, high = 0, len(num) 
        pdb.set_trace()
        
        while low < high:
            
            mid = (low + high)/2
            
            if mid > 0 and mid + 1 < len(num):
                if num[mid] > num[mid - 1] and num[mid] > num[mid + 1]:
                    return mid

                elif num[mid] > num[mid - 1] and num[mid] < num[mid + 1]:
                    low = mid + 1

                else:
                    high = mid - 1

            elif mid == 0:
                if num[mid] > num[1]:
                    return mid

                else:
                    low = mid + 1

            else:
                if num[mid] > num[mid - 1]:
                    return mid

                else:
                    high = mid - 1
        
        return low 
                    
if __name__ == "__main__":
    s = Solution()
    print s.findPeakElement([1, 2, 3])
    print s.findPeakElement([1])
    print s.findPeakElement([1, 2, 3, 1])
    print s.findPeakElement([1, 2, 3, 4, 5, 6, 7, 5])
