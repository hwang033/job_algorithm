import pdb
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if not nums:
            return None
        small, large = self.split(nums)
        print small, large
        pdb.set_trace()
        if len(large) == k - 1:
            return nums[-1]
        if len(large) > k - 1:
            self.findKthLargest(large, k)
        else:
            self.findKthLargest(small, k - len(large) - 1)
    
    def split(self, nums):
        # change with last val
        small = []
        large = []
        for i in range(len(nums)-1):
            if nums[i] < nums[-1]:            
                small.append(nums[i])
            else:
                large.append(nums[i])
        
        return small, large

if __name__ == "__main__":
    s = Solution()
    print s.findKthLargest([2,1], 1)
