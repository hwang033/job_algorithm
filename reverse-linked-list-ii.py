import pdb
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        
        prev_start = start = end = end_next = None
        
        fn1 = ListNode(0)
        fn1.next = head
        
        i = 0
        
        h = fn1
        while i <= n - 1 and h:
            if i == m - 1:
                prev_start = h
                start = h.next
                #prev_start.next = None
            
            h = h.next
            i += 1
        
        if h:
            end = h
            end_next = h.next
            end.next = None

        if not start:
            return head
            
        fn = ListNode(0)
        fn.next = start
        
        p, q, r = fn, start, start.next
        
        while q is not None:
            q.next = p
            p = q
            q = r
            if r is not None:
                r = r.next
        
        prev_start.next = p
        fn.next.next = end_next
        
        return fn1.next

if __name__ == "__main__":

    L1 = ListNode(3)
    L2 = ListNode(5)
    
    L1.next = L2
    L2.next = None 

    rl = Solution() 
    h = rl.reverseBetween(L1, 1, 2)
    while h is not None:
        print h.val
        h = h.next
