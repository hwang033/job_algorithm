#!/usr/lib/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
    # set two pointers, one run one step each time
    # the other run two steps each time, 
        if not head:
            return False

        slow = head
        fast = head.next

        while fast is not None:
            if slow is fast:
                return True

            if fast.next:
                fast = fast.next.next
            else:
                return False

            slow = slow.next
        
        return False


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
    L2.next = L3
    L3.next = L4
    L4.next = L5 
    L5.next = L6
    L6.next = L7 
    L7.next = L8
    L8.next = L9
    L9.next = None 

    rl = Solution() 
    print rl.hasCycle(L1)
        
                
