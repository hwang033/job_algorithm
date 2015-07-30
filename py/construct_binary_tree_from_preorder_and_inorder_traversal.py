#!/usr/lib/python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        #recursive method buld tree
        if not preorder or not inorder:
            return None
        val = preorder[0]
        curnode = TreeNode(val)

        idx = inorder.index(val)
        leftTr = []
        rightTr = []
        if idx+1 <=len(preorder):
            rightTr = preorder[idx+1:]
            leftTr = preorder[:idx+1]
            leftTr.remove(val)
           
        if not leftTr:
            curnode.left = None 
        else:
            curnode.left = self.buildTree(leftTr, inorder[0:idx])

        if not rightTr:
            curnode.right = None
        else:
            curnode.right = self.buildTree(rightTr, inorder[idx+1:])
        
        return curnode

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.left = n2

    s = Solution()
    #print s.buildTree(['a','b','d','e','h','i','c','f','g'],\
    #['d','b','h','e','i','a','f','c','g'])
    print s.buildTree([1,2,3], [3,2,1])

