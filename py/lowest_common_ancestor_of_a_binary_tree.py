# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return root
            
        p_path = []  
        q_path = []
        self.find_element(root, p, p_path)
        self.find_element(root, q, q_path)
        print p_path 
        print q_path
        common = None
        while p_path and q_path and p_path[-1] == q_path[-1]:
            common = p_path[-1]
            print common
            p_path.pop()
            q_path.pop()
        
        return common
        
    
    def find_element(self, root, p, path):
        
        if root == None:
            return False
            
        if root.val == p.val:
            path.append(root.val)
            return True
        
        if self.find_element(root.left, p, path) or self.find_element(root.right, p, path):
            path.append(root.val)
            return True
        else:
            return False

if __name__ == "__main__":
    n1 = TreeNode(1)    
    n2 = TreeNode(2)    

    n1.left = n2
    s = Solution()
    print s.lowestCommonAncestor(n1, n1, n2)



