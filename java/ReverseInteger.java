package leetcode;

public class ReverseInteger {
    public int reverse(int x) {
    	int rst = 0;
    	int base = 10;
    	
    	while(x != 0){
    		if(rst > Integer.MAX_VALUE*1.0/10 || rst < Integer.MIN_VALUE*1.0/10){
    			return 0;
    		}
    		rst *= 10;
    		rst += x % base;
    		x = x/base;    		
    	}
    	
		return rst;
        
    }

	public static void main(String[] args) {
		ReverseInteger ri = new ReverseInteger();
		System.out.println(ri.reverse(1056389759));
	}

}
