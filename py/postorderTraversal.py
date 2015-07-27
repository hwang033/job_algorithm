#Defination for a  binary tree node
import pdb
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
        # @param root, a tree node
        # @return a list of integers
    def postorderTraversal(self, root):
        
        if not root:
            return []

        stack = [root]                
        checked = []
        postorder = []

        while len(stack) is not 0:
            #pdb.set_trace()
            curNode = stack[-1] 
            noChildrenFlag = 0
        
            if checked and curNode is checked[-1]:
                #is stack[-1] was checked before, print it 
                stack.pop()
                checked.pop()
                postorder.append(curNode.val)
                continue

            if curNode.right is not None:
                stack.append(curNode.right)
                noChildrenFlag = 1
                
            if curNode.left is not None:
                stack.append(curNode.left) 
                noChildrenFlag = 1

            if noChildrenFlag is 0: 
                #if this is leaf node, add it to rst
                stack.pop()
                postorder.append(curNode.val)
            else: 
                checked.append(curNode)

        return postorder

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
                
    s = Solution()
    print s.postorderTraversal(a)
