package leetcode;

public class MaximumDepthofBinaryTree {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
    public int maxDepth(TreeNode root) {
    	int depth = 0;
    	if(root == null){
    		return depth;
    	}
    	int left_depth = maxDepth(root.left);
    	int right_depth = maxDepth(root.right);
    	return left_depth > right_depth? (left_depth + 1) : (right_depth + 1);
        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
