import pdb
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        # find the length of headA and headB
        if not headA or not headB:
            return None
        
        l1 = headA
        l2 = headB
        
        len_a = self.get_length(l1)
        len_b = self.get_length(l2)
        diff = abs(len_a - len_b)
        
        l1 = headA
        l2 = headB
        if len_b < len_a:
            l1 = self.get_node(diff, l1)
        else:
            l2 = self.get_node(diff, l2)
            
            
        while l1 is not None and l2 is not None:
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
        
        return None
            
    def get_node(self, step, head):
        
        while step > 0:
            head = head.next
            step -= 1
        return head 
        
    def get_length(self, q):
        
        length = 0
        
        while q is not None:
            q = q.next
            length += 1
        
        return length
if __name__ == "__main__":

    input = [[3], [2,3]]
    node2 = ListNode(2)
    node3 = ListNode(3)
    node2.next = node3

    s = Solution()    
    h = s.getIntersectionNode(node3, node2)
    print h.val







