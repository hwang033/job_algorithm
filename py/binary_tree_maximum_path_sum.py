# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        #using post-order traverse
        
        val, sum_val = self.post_order(root, [])
        return max(sum_val)
        
    def post_order(self, root, sum_val):
        
        if root.left is None and root.right is None:
            return root.val, sum_val

        #print sum_val   
        left_sum = right_sum = 0

        if root.left is not None:
            left_sum, sum_val = self.post_order(root.left, sum_val)

        if root.right is not None:
            right_sum, sum_val = self.post_order(root.right, sum_val)

        
        sum_val.append(left_sum + right_sum + root.val)
        
        return max(left_sum + root.val, right_sum + root.val), sum_val
        
if __name__ == "__main__":
    
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.left = n2

    s = Solution()
    print s.maxPathSum(n1)
