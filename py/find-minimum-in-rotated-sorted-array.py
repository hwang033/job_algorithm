class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        
        high = len(num) - 1
        low = 0
        
        while low < high:
            mid = (low + high)/2
            if num[mid] > num[high]:
                low = mid + 1
            else:
                high = mid
        
        return num[low]

if __name__ == "__main__":
    s = Solution()
    print s.findMin([0,1,2,3,4,5])
