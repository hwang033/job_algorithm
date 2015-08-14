package leetcode;

import java.util.LinkedList;
import java.util.List;

public class PopulatingNextRightPointersinEachNode {

	public class TreeLinkNode {
		int val;
		TreeLinkNode left, right, next;
		TreeLinkNode(int x) { val = x; }
	}
	
    public void connect(TreeLinkNode root) {
    	//level order traversal 
    	 if(root != null){
	    	 List<TreeLinkNode> queue = new LinkedList<TreeLinkNode>();
	    	 queue.add(root);
	    	 TreeLinkNode prev = null;
	    	 while(queue.size() != 0){
	    		 List<TreeLinkNode> n_queue = new LinkedList<TreeLinkNode>();
	    		 for(TreeLinkNode n: queue){
	    			 if(prev != null){
	    				 prev.next = n;
	    			 }
	    			 prev = n;
	    			 if(n.left != null){
	    				 n_queue.add(n.left);
	    			 }
	    			 if(n.right != null){
	    				 n_queue.add(n.right);
	    			 }	 
	    		 }
	    		 queue = n_queue; 
	    		 prev = null;
	    	 }
    	 }
    }
    public void connect2(TreeLinkNode root) {
    	if(root == null){
    		return;
    	}
    	if(root.left != null){
    		root.left.next = root.right;
    	}
    	if(root.next != null && root.next.left != null){
    		root.right.next = root.next.left;
    	}
    	connect2(root.left);
    	connect2(root.right);

    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
