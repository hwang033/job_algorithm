class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_dup(head):
    dummy = Node(0)
    dummy.next = head
    cur = dummy

    has_val = set([])

    #while cur is not None and  cur.next is not None:
    while cur.next is not None:
        if cur.next.val in has_val: 
            cur.next = cur.next.next
        else:
            has_val.add(cur.next.val)
            cur = cur.next
    return dummy.next

def remove_dup2(head):
    dummy = Node(0)
    dummy.next = head
    cur = dummy

    has_val = set([])

    while cur.next is not None:
        prev = dummy.next
        while prev is not cur.next:
            if cur.next.val == prev.val: 
                cur.next = cur.next.next
                break
            prev = prev.next
        else:
            cur = cur.next

    return dummy.next
if __name__ == "__main__":
    #vals = [1,2,3,4,2]
    #vals = [1,1,1,1]
    #vals = [1]
    vals = []
    #vals = [1,1,1,2,2,4,4,3,2,2]
    ln = head = Node(0)
    for val in vals:
        ln.next = Node(val)
        ln = ln.next

    head = remove_dup2(head.next)
    while head is not None:
        print head.val
        head = head.next



    
