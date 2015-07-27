#!/usr/lib/python
import pdb
class RandomListNode:

     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        
        if not head:
            return None
        
        randdict = {} 
        randlist = []
        h = head 
        idx = 0

        while(h is not None):
            randlist.append(h)
            randdict[h] = idx
            idx += 1
            h = h.next

        copylist = [RandomListNode(n.label) for n in randlist]

        copylist.append(None)

        for i in range(idx):     
            copylist[i].next = copylist[i+1] 
            if randlist[i].random:
                ranidx = randdict[randlist[i].random]
                copylist[i].random = copylist[ranidx]
            else:
                copylist[i].random = None

        return copylist[0]


            
             
if __name__ == "__main__": 

    L1 = RandomListNode(1)
    L2 = RandomListNode(2)
    L3 = RandomListNode(3)
    L4 = RandomListNode(4)
    L5 = RandomListNode(5)
    L6 = RandomListNode(6)
    L7 = RandomListNode(7)
    L8 = RandomListNode(8)
    L9 = RandomListNode(9)
    
    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = L5 
    L5.next = L6
    L6.next = L7 
    L7.next = L8
    L8.next = L9
    L9.next = None 

    L1.random = L2
    L2.random = L3
    L3.random = L4
    L4.random = L5 
    L5.random = L6
    L6.random = L7 
    L7.random = L8
    L8.random = L9
    L9.random = None 

    rl = Solution() 
    head =  rl.copyRandomList(L1)
    while  head is not None:
        print head.label
        head = head.random
        
                
    
            

          
