package leetcode;

public class MaximumSubarray {
    public int maxSubArray(int[] nums) {
    	int sum = 0;
    	int maxsum = Integer.MIN_VALUE;
    	for(int i: nums){
    		
    		if(sum + i < i){
    			sum = i;
    		}
    		else{
    			sum += i;
    		}
    		maxsum = sum > maxsum? sum: maxsum;
    		
    	}
    	return maxsum;
        
    }
	public static void main(String[] args) {
		MaximumSubarray ms = new MaximumSubarray();
		int[] nums = new int[]{-2,-3,-1,-5};
		System.out.print(ms.maxSubArray(nums));

	}

}
