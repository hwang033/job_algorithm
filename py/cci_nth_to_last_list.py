import pdb
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_nth_to_last(head, n):
    dummy = Node(0)
    dummy.next = head
    
    fast = slow = dummy
    step = 0 
    while fast.next is not None and step < n:
        fast = fast.next
        step += 1

    #if n > length of the list
    if step < n:
        return None 
    
    while fast is not None:
        fast = fast.next
        slow = slow.next 

    return slow.val

def delete_node(n):       
    #if n is not the last node
    if n is None or n.next is None:
        return False

    n.val = n.next.val
    n.next = n.next.next
    return True
    
if __name__ == "__main__":

    vals = [6,5,4,3,2,1]
    ln = head = Node(0)
    for val in vals:
        ln.next = Node(val)
        ln = ln.next
         
    while head is not None:
        head = head.next

