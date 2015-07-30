#!/usr/bin/python
import pdb

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    
    def inorderTraversalRecursive(self, root, rst = []):
        #visit current node
        if root is not None:
            self.inorderTraversal(root.left, rst)
            rst.append(root.val)
            self.inorderTraversal(root.right, rst)
        return rst

    
    def inorderTraversal(self, root):
        
        stack = [] 
        rst = []
        cur = root

        while cur is not None:
            stack.append(cur)
            cur = cur.left

        while stack:
            cur = stack.pop()
            rst.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
                next = cur.right.left
                while next is not None:
                    stack.append(next)
                    next = next.left
                    
        return rst
    
        
if __name__ == "__main__":
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    g = TreeNode('g')
    h = TreeNode('h')
    i = TreeNode('i')
    
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = h
    e.right = i
    c.left = f
    c.right = g
                
    one = TreeNode(1)
    two = TreeNode(2)
    one.right = two
    
    s = Solution()
    print s.inorderTraversal(one)
    print s.inorderTraversal(a)


