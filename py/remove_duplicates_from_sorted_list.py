#!/usr/lib/python/

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        
        if not head:
            return head
        
        n = head
        
        while n is not None:
            if (n.next is not None) and (n.val is n.next.val):
                #remove n.next
                nn = n.next
                n.next = n.next.next
                del nn
            else:
                n = n.next
                
        return head

if __name__ =="__main__":
    s = Solution()

    s.deleteDuplicates(head)

    while head is not None:
        print head.val
        head = head.next
                            
                            
                            
                           
