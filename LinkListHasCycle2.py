#!/usr/lib/python

#definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):

        if not head:
            return None

        slow = head
        fast = head.next
        hasCycle = 0

        while fast is not None:

            if slow is fast:
                hasCycle = 1
                break

            if fast.next is not None:
                fast = fast.next.next
            else:
                return None

            slow = slow.next
            
        if hasCycle:
            h = head
            while h is not slow.next:
               h = h.next 
               slow = slow.next
            return h
        return None

if __name__ == "__main__": 

    L1 = ListNode(1)
    L2 = ListNode(2)
    L3 = ListNode(3)
    L4 = ListNode(4)
    L5 = ListNode(5)
    L6 = ListNode(6)
    L7 = ListNode(7)
    L8 = ListNode(8)
    L9 = ListNode(9)
    
    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = L5 
    L5.next = L6
    L6.next = L7 
    L7.next = L8
    L8.next = L9
    L9.next = L5 

    rl = Solution() 
    print rl.detectCycle(L1).val

