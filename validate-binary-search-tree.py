import pdb
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        # use in-order traversal
        if root == None:
            return True
        pdb.set_trace() 
        if root.left is not None and root.val <= root.left:
            return False
            
        if root.right is not None and root.val >= root.right:
            return False
        
        lt = self.isValidBST(root.left)
        rt = self.isValidBST(root.right)

        
        return (lt and rt)

if __name__ == "__main__":
    r1 = TreeNode(1)
    r2 = TreeNode(1)
    r1.left = r2

    s = Solution()
    print s.isValidBST(r1)

