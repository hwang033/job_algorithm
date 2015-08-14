package leetcode;

public class InvertBinaryTree {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
    public TreeNode invertTree(TreeNode root) {
    	if(root == null){
    		return null;
    	}
    	if(root.left != null){
    		invertTree(root.left);
    	}
    	if(root.right != null){
    		invertTree(root.right);
    	}
    	
    	if(root.left != null && root.right != null){
    		TreeNode n;
    		n = root.left;
    		root.left = root.right;
    		root.right = n;
    	}
    	
        return root;
    }
    
    public TreeNode invertTree2(TreeNode root) {
    	if(root == null){
    		return root;
    	}
    	TreeNode n = root.left;
    	root.left = invertTree2(root.right);
    	root.right = invertTree2(n);
    	
        return root;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
