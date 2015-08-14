package leetcode;

import java.util.ArrayList;
import java.util.HashMap;

public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
    	//KMP method
    	int rst = 0;
    	int[] prev_idx = new int[s.length()];
    	HashMap<Character, Integer> prevIdx = new HashMap<Character, Integer>();
    	
    	for(int i=0; i < s.length(); i ++){
    		if(prevIdx.containsKey(s.charAt(i))){
    			prev_idx[i] = prevIdx.get(s.charAt(i));
    			prevIdx.put(s.charAt(i), i);   			
    		}else{
    			prev_idx[i] = -1;
    			prevIdx.put(s.charAt(i), i);
    		}
    	}
    	
    	int start = -1;
    	for(int i=0; i < s.length(); i ++){
    		if(prev_idx[i] > start){
    			start = prev_idx[i];    		
    		}
    		rst = (rst>(i-start)?rst:(i-start)); 
    	}
    	
    	return rst;
        
    }
	public static void main(String[] args) {
    	LongestSubstringWithoutRepeatingCharacters lswrc = new LongestSubstringWithoutRepeatingCharacters();
    	System.out.println(lswrc.lengthOfLongestSubstring("abcdabcbb"));
    }
}
