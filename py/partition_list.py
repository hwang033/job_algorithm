#!/usr/lib/python
import pdb
#defition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        
        fn = ListNode(0)
        fn.next = head
        less = fn
        prev = fn
        c = head
        while c is not None:
            
            if c.val < x:
                if less.next is not c:
                    prev.next = c.next
                    c.next = less.next
                    less.next = c
                    less = c
                    c = prev.next 
                else:
                    less = c
                    prev = c
                    c = c.next
            else:
                prev = c
                c = c.next
                
        return fn.next

if __name__ == "__main__":
    s = Solution()
    L1 = ListNode(1)
    L2 = ListNode(1)
    L3 = ListNode(3)
    L4 = ListNode(4)
    L5 = ListNode(2)
    L6 = ListNode(3)
    L7 = ListNode(2)
    L8 = ListNode(2)
    L9 = ListNode(5)
    
    L1.next = L2 
    L2.next = None 
   # L3.next = L4
   # L4.next = L5 
   # L5.next = L6
   # L6.next = L7 
   # L7.next = L8
   # L8.next = L9
   # L9.next = None 
    rst = s.partition(L1, 2)                
    while rst:
        print rst.val
        rst = rst.next
