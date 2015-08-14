package leetcode;

public class TwoSumII {
	
    public int[] twoSum(int[] numbers, int target) {
        int[] rst = new int[2];
        int low = 0;
        int high = numbers.length - 1;
        int sum = 0;
        while(low < high){
        	sum = numbers[low] + numbers[high];
        	if (sum > target){
        		high -= 1;
        	}
        	if(sum < target){
        		low += 1;
        	}
        	if(sum == target){
        		rst[0] = low + 1;
        		rst[1] = high + 1;
        		break;
        	}
        }
        return rst;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
