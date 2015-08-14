package leetcode;

public class RemoveDuplicatesfromSortedList {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
    public ListNode deleteDuplicates(ListNode head) {
    	ListNode dummy = new ListNode(0);
    	dummy.next = head;
    	ListNode p = dummy;
    	while(p != null && p.next != null && p.next.next != null){
    		if(p.next.val == p.next.next.val){
    			p.next = p.next.next;
    		}
    		else{
    			p = p.next;
    		}
    		
    	}
    	return dummy.next;
        
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
