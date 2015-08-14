package leetcode;


import java.util.Arrays;

public class MajorityElement {
    
	public int majorityElement(int[] nums) {
		Arrays.sort(nums);
		int mid = nums.length/2;
		return nums[mid];
        
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
