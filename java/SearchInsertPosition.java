package leetcode;

public class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
    	//binary search
    	int low = 0;
    	int high = nums.length - 1;
    	int mid = 0;
    	
    	while(low <= high){
    		mid = (low + high)/2;
    		if(nums[mid] == target){
    			return mid;
    		}
    		if(nums[mid] > target){
    			high = mid - 1;
    		}
    		else{
    			low = mid + 1;
    		}
    	}
    	return  low;
        
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SearchInsertPosition sip = new SearchInsertPosition();
		int[] nums = new int[]{1,3,5,6};
		System.out.println(sip.searchInsert(nums, 0));
	}

}
