package leetcode;

public class LinkedListCycle {
	class ListNode {
		int val;
		ListNode next;
		ListNode(int x) {
		val = x;
		next = null;
		}
	}
	
    public boolean hasCycle(ListNode head) {
    	ListNode dummy = new ListNode(0);
    	dummy.next = head;
    	
    	ListNode fast = dummy;
    	ListNode slow = dummy;
    	
    	while(fast != null && fast.next !=null){
    		fast = fast.next.next;
    		slow = slow.next;
    		if(fast == slow){
    			return true;
    		}
    	}
    	return false;    	
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
