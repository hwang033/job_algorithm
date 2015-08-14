package leetcode;

import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {
	
    public boolean containsDuplicate(int[] nums) {
    	Set<Integer> contains = new HashSet<Integer>();
    	for(int i : nums){
    		if(contains.contains(i)){//!contains.add(i) contains.add return False
    			return true;
    		}
    		contains.add(i);
    	}
        return false;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[]{1,2,3,4,5};		
		ContainsDuplicate cd = new ContainsDuplicate();
		System.out.print(cd.containsDuplicate(nums));
	}

}
