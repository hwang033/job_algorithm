package leetcode;

public class PalindromeNumber {
    public boolean isPalindrome(int x) {
    	int rst = 0;
    	int base = 10;
    	int val = x;
    	
    	while(val != 0){
    		if(rst > Integer.MAX_VALUE*1.0/10 || rst < Integer.MIN_VALUE*1.0/10){
    			return false;
    		}
    		rst *= 10;
    		rst += val % base;
    		val = val/base;    		
    	}
    	
    	if(rst == x){
    		return true;
    	}
		return false;     
    	
    }

	public static void main(String[] args) {
		PalindromeNumber pm = new PalindromeNumber();
		System.out.println(pm.isPalindrome(12321));
	}
}
