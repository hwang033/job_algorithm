package leetcode;

public class SingleNumber {
	
	 public int singleNumber(int[] nums) {
		int rst = 0;
		for(int i: nums){
			rst ^= i;
		}
		return rst;
	        
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SingleNumber sn = new SingleNumber();
		int[] nums = {1,1,2};
		System.out.println(sn.singleNumber(nums));
	}

}
