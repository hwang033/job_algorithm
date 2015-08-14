package leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BinaryTreeInorderTraversal {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
    public List<Integer> inorderTraversal(TreeNode root) {
    	List<Integer> rst = new ArrayList<Integer>();
    	Stack<TreeNode> st = new Stack<TreeNode>();
    	
      	TreeNode cur = root;
    	while(cur != null){
    		st.push(cur);
    		cur = cur.left;
    	}
    	
    	st.push(root);
    	while(!st.isEmpty()){
    		cur = st.pop();
    		rst.add(cur.val);
    		if(cur.right != null){
    			cur = cur.right;
    			while(cur != null){
    				st.push(cur);
    				cur = cur.left;
    			}
    		}    		
    	}
    	return rst;
    				
        
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
