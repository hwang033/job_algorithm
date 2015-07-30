import pdb
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    
    def buildTreeRecursive(self, inorder, postorder):
        # first try copy inorder and postorder but failed
        if not inorder or not postorder:
            return None
        return self.helper(inorder, postorder, 0, len(inorder) - 1,\
                0, len(postorder) - 1)
    
    def helper(self, inorder, postorder, in_s, in_e, po_s, po_e):
        if in_s > in_e or po_s > po_e:
            return None
            
        root_val = postorder[po_e]
        
        if root_val == 4:
            pdb.set_trace()
        idx = inorder.index(root_val)
         
        root.left = self.helper(inorder, postorder, in_s, idx-1, po_s,\
                    po_s + idx - in_s - 1)
        root.right = self.helper(inorder, postorder, idx + 1, in_e,\
                    po_s + idx - in_s, po_e -1)
        
        return root
   
    def buildTree(self, inorder, postorder):
        # this solution is from other
        if len(inorder) == 0:
            return None
            
        root = TreeNode(postorder.pop())
        stn = list()
        stn.append(root)

        while True:

            if inorder[-1] == stn[-1].val:
                # deal with left tree
                p = stn.pop()
                inorder.pop()

                if len(inorder) == 0:
                    break
                
                if len(stn) != 0 and inorder[-1] == stn[-1].val:
                    # if meet the ancestor
                    continue

                p.left = TreeNode(postorder.pop())
                stn.append(p.left)
            else:
                # Right sub-tree
                p = TreeNode(postorder.pop())
                stn[-1].right = p
                stn.append(p)

        return root
        
         

if __name__ == "__main__":        
    s = Solution()
    root = s.buildTree([1,2,3,4], [1,3,4,2])
    #root = s.buildTree([1,2,3,4,5,6], [1,2,5,6,4,3])
    #root = s.buildTree([4,2,5,1,6,7,3], [4,5,2,7,6,3,1])

    while root:
        print root.val
        root = root.left
        
        
