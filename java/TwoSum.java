package leetcode;

import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] rst = new int[2];
        HashMap<Integer, Integer> hasValue = new HashMap<Integer, Integer>();
        int diff;
        
        for(int i=0; i<nums.length; i++){
        	diff = target - nums[i];
        	if(hasValue.containsKey(diff)){
        		rst[0] = hasValue.get(diff) + 1;
        		rst[1] = i + 1;
        	}else{
        		hasValue.put(nums[i], i);
        	}     	
        	
        }
        
        return rst;
    }

	public static void main(String[] args) {
		int[] nums = {2, 7, 11, 15};
		int target = 9;
		TwoSum ts = new TwoSum();
		int[] rst = ts.twoSum(nums, target);
		System.out.println(rst[0] + " " + rst[1]);
		
		

	}

}
