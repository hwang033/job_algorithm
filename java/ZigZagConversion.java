package leetcode;

public class ZigZagConversion {
    public String convert(String s, int numRows) {
        if(numRows == 1){
            return s;
        }
        String rst = "";
    	int step2 = (numRows - 1)*2;
    	int step1 = 0;
    	for(int i=0; i<numRows; i++){
    		step1 = (numRows - i - 1)*2;
    		int j = i;
    		if(j < s.length()){
    		    rst += s.charAt(j);
    		}
    		while(j < s.length()){
    			
    			if(j + step1 < s.length() && step1 != 0){
    				rst += s.charAt(j + step1);
    			}
    			if(j + step2 < s.length() && step1 != step2){
    				rst += s.charAt(j + step2);
    			}
    			j += step2;
    		}
    	}
    	
    	return rst;
    }
	public static void main(String[] args) {
		
		ZigZagConversion zzc = new ZigZagConversion();
		System.out.println(zzc.convert("PAYPALISHIRING", 3));
		System.out.println(zzc.convert("AB", 1));
		

	}

}
