#!/usr/lib/python
import pdb
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
        # @param head, a ListNode
        # @return nothing
    def reorderList(self, head):

        if not head or not head.next:
            return head 
       
        half = head
        h = head
        #get middle of the list O(n)
        while h.next.next is not None:
            half = half.next
            h = h.next.next
        hn = half.next
        half.next = None
        half = hn

        #reverse half list O(n)
        fakeh = ListNode(0)
        fakeh.next = half
        p = fakeh
        q = half
        r = half.next

        while r is not None:
            q.next = p
            p = q
            q = r
            r = r.next

        q.next = p
        fakeh.next.next = None

        #merge two list o(N)
        l = head
        while l.next is not None:
            qn = q.next
            q.next = l.next
            l.next = q
            l = l.next.next
            q = qn
        if q is not None:
            l.next = q
        return head


if __name__ == "__main__":
    
    L1 = ListNode(1)
    L2 = ListNode(2)
    L3 = ListNode(3)
    L4 = ListNode(4)
   # L5 = ListNode(2)
   # L6 = ListNode(3)
   # L7 = ListNode(2)
   # L8 = ListNode(2)
   # L9 = ListNode(5)
    
    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = None 
   # L5.next = L6
   # L6.next = L7 
   # L7.next = L8
   # L8.next = L9
   # L9.next = None 

    rl = Solution() 
    head = rl.reorderList(L1)
    while head :
        print head.val
        head = head.next
    

