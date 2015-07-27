class Solution:

    # @param height, a list of integer

    # @return an integer

    def largestRectangleArea(self, height):

        #O(n^2)

        if not height:
            return height
        low = 0
        high = len(height) - 1
        maxarea = None
        while low <= high:
            area = min(height[low:high + 1])*(high - low + 1)
            if maxarea is None or maxarea < area:
                maxarea = area

            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1

        return maxarea

if __name__ == "__main__":
    s = Solution()
    print s.largestRectangleArea([2,1,5,6,2,3])
