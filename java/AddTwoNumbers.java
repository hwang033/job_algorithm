package leetcode;

public class AddTwoNumbers {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
		}
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
		ListNode p = l1;
		ListNode q = l2;
		ListNode r = dummy;
		int carry = 0;
		int sum = 0;
		while(p != null && q != null){
			sum = p.val + q.val + carry;
			carry = sum / 10;
			r.next = new ListNode(sum % 10);
			r = r.next;
			p = p.next;
			q = q.next;
		}
		ListNode left = (p!=null?p:q);
		while(left != null){
			sum = left.val + carry;
			carry = sum / 10;
			r.next = new ListNode(sum % 10);
			r = r.next;
			left = left.next;
		}
		
		if(carry != 0){
			r.next = new ListNode(carry);
		}
		return dummy.next;
        
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
