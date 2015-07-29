class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        # bianry search
        low = 0
        high = len(nums) - 1
        rst = 0
        while low <= high:
            mid = (low + high)/2
            print low, high, mid, nums[mid]
            if nums[mid] > target:
                high = mid - 1
                #rst = (mid - 1 if mid > 0 else 0)
                rst = mid
            elif nums[mid] < target:
                low = mid + 1
                rst = mid + 1
            else:
                rst = mid
                break
            
        return rst

if __name__ == "__main__":
    s = Solution()
    print s.searchInsert([1, 3], 2)
    print s.searchInsert([1,3,5,6], 5)
    print s.searchInsert([1,3,5,6], 2)
    print s.searchInsert([1,3,5,6], 7)
    print s.searchInsert([1,3,5,6], 0)
    print s.searchInsert([1,3,5,6], 5.5)

