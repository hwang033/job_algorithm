#!/usr/bin/python
import pdb

# Sort a linked list in O(n log n) time using constant space complexity.
# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def sortList(self, head):
    #sort from small to big    
    #using merge sort 
        if not head or not head.next:
            return head
           
        right = head
        left = head
        prev = head 
         
        if not head.next.next: 
            left = head.next   

        else:
            while right.next is not None and right.next.next is not None:
                right = right.next.next
                prev = left
                left = left.next

        prev.next = None 
        right = head
        #recursivly sort half list
        ll = self.sortList(left)
       # print "calling ll"
       # llc = ll
       # while llc is not None:
       #     print llc.val
       #     llc = llc.next
        lr = self.sortList(right)
       # print "calling lr"
       # llc = lr
       # while llc is not None:
       #     print llc.val
       #     llc = llc.next

       # print "end calling"
        return self.merge(ll, lr)
 
    def merge(self, ll, lr):
        
        #pdb.set_trace()
        head = None 
        while lr is not None and ll is not None: #not finish 

            if ll.val > lr.val:
               #insert lr to the front of ll 
               lrn = lr.next
               lr.next = ll 
               ll = lr
               if head == None:
                   head = ll
               lr = lrn

            elif ll.next is None:
               if head == None:
                   head = ll
               ll.next = lr 
               ll = None 

            elif ll.next.val >= lr.val:
            #insert lr between ll and ll.next               
               if head == None:
                   head = ll
               lrn = lr.next
               lr.next = ll.next
               ll.next = lr

               lr = lrn
               ll = ll.next #move lr
            else:   
               if head == None:
                   head = ll
               ll = ll.next

           
        return head 
       
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
    head = listsort.sortList({})
    while head :
        print head.val
        head = head.next


    
