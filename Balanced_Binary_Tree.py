#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
                
        #return False if self.height(root) is False else True 
        return self.height(root) 
        
    
    def height(self, node):
        
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return 1
        lh = self.height(node.left)
        lr = self.height(node.right)

        print node.val
        print lh 
        print lr 
        
        if lh is False or lr is False:
            return False
            
        elif lh - lr >= 2 or lh - lr <= -2:
            return False
        
        return max(lh + 1 , lr + 1)

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.left = n2

    s = Solution()
    print s.isBalanced(n1)

