# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        root = self.helper(num, 0, len(num) - 1)
        return root
        
    def helper(self, num, start, end):

        if start > end:
            return None
        
        mid = (start + end)/2
        node = TreeNode(0)
        node.left = self.helper(num, start, mid - 1 )
        node.val = num[mid]
        node.right = self.helper(num, mid + 1, end)
        
        return node

    def layer_traversal(self, root):
        
        buffer = [root]
        while buffer:
            new_buffer = []
            output = []
            for x in buffer:
                output.append(str(x.val))
                if x.left is not None:
                    new_buffer.append(x.left)
                if x.right is not None:
                    new_buffer.append(x.right)
            print ' '.join(output)
            buffer = new_buffer

if __name__ == "__main__":
    s = Solution()
    l = [1,2,3,4,5,6,7]
    root = s.sortedArrayToBST(l)
    s.layer_traversal(root)
