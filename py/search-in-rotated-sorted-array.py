import pdb
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        #find the rotate place
        print nums, target    
        low = 0
        high = len(nums) - 1

        while low < high:
            #pdb.set_trace()
            mid = (low + high)/2
            if nums[mid] > nums[high]:
                low = mid + 1 
            else:
                high = mid
        
        rot = low #if (low < len(nums) - 1) and (nums[low] < nums[low + 1]) else low + 1 #low + 1

       # if low < len(nums) - 1 and nums[low] > nums[low + 1]: 
       #     rot += 1
        print low, rot

        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high)/2
            realmid = (mid + rot)%len(nums)
            if nums[realmid] == target:
                return realmid 
            elif nums[realmid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1

if __name__ == "__main__":        
    s = Solution()
    print s.search([1,2,3,4,5,6,7,8], 6)
    print s.search([6,7,8,1,2,3,4], 6)
    print s.search([3, 1], 1)
    print s.search([1, 3], 1)
    print s.search([5, 1, 3], 5)
    print s.search([4, 5, 6, 1, 3], 5)
    print s.search([5, 6, 1, 3], 5)

