class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_binary_tree_from_list(l): 
    if not l:
        return None

    mid = len(l)/2
    root = Node(l[mid])
    root.left = create_binary_tree_from_list(l[:mid])
    root.right = create_binary_tree_from_list(l[mid+1:])
    return root

def tree_traverse(root, des="root"):
    if root == None:
        return
    print root.val, des
    tree_traverse(root.left, "%s' left" %root.val)
    tree_traverse(root.right, "%s's right" %root.val)

if __name__ == "__main__":
    root = create_binary_tree_from_list([1,2,3,4,5])
    tree_traverse(root)
    
