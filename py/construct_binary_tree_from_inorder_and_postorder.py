#!/usr/lib/python/
#defition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
     
        if not inorder or not postorder:
            return None
        
        parentval = postorder.pop()
        parent = TreeNode(parentval)
        idx = inorder.index(parentval)
        
        leftpost = postorder[:idx]
        rightpost = postorder[idx:]
        
        if leftpost:
            parent.left = self.buildTree(inorder[:idx], leftpost)
        else:
            parent.left = None
        
        if rightpost:
            parent.right = self.buildTree(inorder[idx+1:], rightpost)    
        else:
            parent.right = None
            
        return parent
        
        
if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.left = n2

    s = Solution()
    #print s.buildTree(['a','b','d','e','h','i','c','f','g'],\
    #['d','b','h','e','i','a','f','c','g'])
    print s.buildTree([2,1,3], [2,3,1])

