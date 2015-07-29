import pdb
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        
        area1 = abs(A-C)*abs(B-D)
        area2 = abs(E-G)*abs(F-H)
        #intersect
        length = [A, C, E, G]
        height = [D, B, H, F]
        intersect = 0
        if self.has_intersect(A, C, E, G) and self.has_intersect(B, D, F, H):
            length.sort()
            height.sort()
            intersect = (length[2] - length[1]) * (height[2] - height[1])
        
        print area1, area2, intersect 
        return area1 + area2 - intersect
        
    def has_intersect(self, A, C, E, G):
        pdb.set_trace() 
        if  A <= E <= C:
            return True
        if A <= G <= C:
            return True

if __name__ == "__main__":
    s = Solution()        
    #print s.computeArea(-2, -2, 2, 2, -2, -2, 2, 2)
    print s.computeArea(-2, -2, 2, 2, -3, -3, 3, -1)
