#!/usr/lib/python
import pdb

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head:
            return head
            
        fn = ListNode(0)
        fn.next = head
        h=t=fn
        count = -1
        while t is not None:

            t = t.next
            count += 1

            if count%k == 0 and count != 0:
                p = h
                nh = q = h.next
                r = h.next.next
                q.next = t #first node point to tail.next
                if k > 1: 
                    while q is not t:
                        p = q
                        q = r
                        r = r.next if r is not None else None
                        if q is not t:
                            q.next = p
                if p is not h:    
                    h.next = p
                h = nh

                #f = fn
                #while f is not None:
                #    print f.val
                #    f = f.next
                #print "#"
                
        return fn.next

if __name__ == "__main__": 

    L1 = ListNode(1)
    L2 = ListNode(2)
    L3 = ListNode(3)
    L4 = ListNode(4)
    L5 = ListNode(2)
    L6 = ListNode(3)
    L7 = ListNode(2)
    L8 = ListNode(2)
    L9 = ListNode(5)
    
    L1.next = L2 
    L2.next =  None 
    #L2.next = L3 
    #L3.next = L4
    #L4.next = None 
    #L5.next = None 
    #L5.next = L6
    #L6.next = L7 
    #L7.next = L8
    #L8.next = L9
    #L9.next = None 

    r = Solution() 
    rst = r.reverseKGroup(L1, 1)
    
    while rst is not None:
        print rst.val
        rst = rst.next
        

