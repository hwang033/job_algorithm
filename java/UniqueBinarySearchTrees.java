package leetcode;

public class UniqueBinarySearchTrees {

	public int numTrees(int n) {
		//Dynamic programming
		// f[i] = f[i-k] + f[k-1]
		if(n == 0){
			return 0;
		}
		int[] f = new int[n + 1];
		f[0] = 1;
		f[1] = 1;
		for(int i = 2; i <= n; i ++){
			for(int j = 1; j <= i; j ++){
				f[i] += f[i-j]*f[j-1];
			}
		}
		return f[n];
		
		
    }

	public static void main(String[] args) {
		UniqueBinarySearchTrees ubst = new UniqueBinarySearchTrees();
		System.out.print(ubst.numTrees(3));

	}

}
