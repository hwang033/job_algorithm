#!/usr/lib/python
#definition for a  binary tree node
import pdb
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        #using preorder
        if not root:
            return []
        sumval = sum
        rst = []
        stackpath = [[root.val]]
        stack = [root]
        
        while stack:
            curn = stack.pop()
            curs = stackpath.pop()
            pdb.set_trace()
            if curn.right is not None:
                stack.append(curn.right)
                stackpath.append(curs[:].append(curn.right))
            if curn.left is not None:
                stack.append(curn.left)
                stackpath.append(curs[:].append(curn.left))
            if curn.right is None and curn.left is None:
                if sum(curs) == sumval:
                    rst.append(curs)
        return rst

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.left = n2

    s = Solution()
    print s.pathSum(n1, 0)

