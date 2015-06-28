#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        
        if not head.next or not head:
            return head

        cur = head.next
        prev = head
        

        while cur is not None:


            prev_pos, pos = self.findPos(cur, head)

            if pos == cur:
                prev = cur
                cur = cur.next
                continue

            next = cur.next
            prev.next = next
            cur.next = pos 

            if pos == head:
                head = cur 
            else:
                prev_pos.next = cur

            cur = next
          #  print "sort"
          #  llc = head
          #  while llc is not None:
          #      print llc.val
          #      llc = llc.next
             
        return head

    def findPos(self, cur, head):
        
        prev = None
        while head is not cur:
            if head.val > cur.val:
                return prev, head
            else:
                prev = head
                head = head.next
        return prev, cur
 

if __name__ == "__main__":
    L1 = ListNode(2)
    L2 = ListNode(4)
    L3 = ListNode(1)
    L4 = ListNode(2)
    L5 = ListNode(2)
    L6 = ListNode(3)
    L7 = ListNode(2)
    L8 = ListNode(2)
    L9 = ListNode(5)
    
    L3, L2 = L2, L3 
    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = L5
    L5.next = L6
    L6.next = L7 
    L7.next = L8
    L8.next = L9
    L9.next = None 
    

    listsort = Solution() 
    #head = listsort.insertionSortList(L1)
    head = L1
    
    while head :
        print head.val
        head = head.next




