class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

def lca(root, p, q):
    #check is p and q are in the tree or not 
    if root == None:        
        return None
    if root == p or root == q:
        return root

    l = lca(root.left, p, q)
    r = lca(root.right, p, q)
    
    if l and r:
        return root, True
    if (not l) and (not r):
        return None
    return l if l is not None else r


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n2.right = n4
    print lca(n1, n5, n3).val
