class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def linked_list(self, root):
    if not root: 
        return

    new_q = queue = [root]


    while queue:
        cur = queue.pop(0)
        if prev != None:
            prev.next = cur

        prev = cur

        if cur.left is not None:
            new_q.append(cur.left)

        if cur.right is not None:
            new_q.append(cur.right)

        if not queue:
            if not new_q:
                break
            queue = new_q     
            prev = None 
            new_q = []



