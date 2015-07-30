# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root, level = 1, rst = [[]]):
        # try recursive method
        if root != None and len(rst) < level:
            rst.append([])
            
        if root != None:
            self.levelOrderBottom(root.left, level + 1, rst)
            self.levelOrderBottom(root.right, level + 1, rst)
            nl = len(rst) - level
            rst[nl].append(root.val)
        
        return rst

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2

    s = Solution()
    print s.levelOrderBottom(n1)
