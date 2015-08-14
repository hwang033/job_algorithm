package leetcode;

import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class BinaryTreePreorderTraversal {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> rst = new LinkedList<Integer>();
        Stack<TreeNode> st = new Stack<TreeNode>();
        st.add(root);
        while(!st.isEmpty()){
        	TreeNode cur = st.pop();
        	rst.add(cur.val);
        	if(cur.right != null){
        		st.add(cur.right);
        	}
        	if(cur.left != null){
        		st.add(cur.left);
        	}
        }     
        return rst;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
