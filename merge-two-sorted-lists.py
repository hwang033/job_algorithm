import pdb
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        dummy = ListNode(0)
        
        dummy1.next = l1
        dummy2.next = l2
        
        p1 = dummy1
        p2 = dummy2
        p = dummy
        
        while (p1.next is not None) and (p2.next is not None):
            #pdb.set_trace() 
            if p1.next.val <= p2.next.val:
                p.next = ListNode(p1.next.val)
                p1 = p1.next
            else:
                p.next = ListNode(p2.next.val)
                p2 = p2.next
     
            p = p.next
        
        if p1.next is not None:
            p.next = p1.next
         
        elif p2.next is not None:
            p.next = p2.next
            
        return dummy.next

if __name__ == "__main__":
    input = [[-10,-10,-9,-4,1,6,6], [-7]]
    rst = []
    for l in input:
        dummy = ListNode(0)
        q = dummy
        for num in l:
            q.next = ListNode(num)
            q = q.next
        rst.append(dummy.next) 

    s = Solution()    
    h = s.mergeTwoLists(rst[0], rst[1])
    while h is not None:
        print h.val 
        h = h.next 







