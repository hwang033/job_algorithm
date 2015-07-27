#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head, end = None): #t(n) = 2t(n/2) + o(n) = O(nlogn) 
        #recrusive method
        
        if head == end:
            return None
        
        if head.next == end:
            return TreeNode(head.val)
            
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        
        while fast is not end and fast.next is not end:
            fast = fast.next.next
            slow = slow.next
            
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head, slow)
        node.right = self.sortedListToBST(slow.next, end)
        
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
    cur = head = ListNode(l[0])
    for i in l[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    
    root = s.sortedListToBST(head)
    s.layer_traversal(root)
    
    



    





