package leetcode;

public class StringtoInteger {
   
	public int myAtoi(String str) {

		//str = str.replaceAll(" ", "");
		str = str.trim();
		int rst = 0;
		int minus = 1;
		int i = 0;
		
        if(str.length() == 0){
            return 0;
        }
		
        if(str.charAt(0) == '-'){
			minus = -1;
			i = 1;
		}

		if(str.charAt(0) == '+'){
			minus = 1;
			i = 1;
		}

		
		for(; i < str.length(); i++){
			if(!Character.isDigit(str.charAt(i))){
				break;
			}
				
			if(minus == 1 && rst > 1000000000){
				return Integer.MAX_VALUE; 
			}
				
			if(minus == -1 && minus*rst < -1000000000){
				return Integer.MIN_VALUE;
			}
			rst *= 10;
			if(minus== 1 && (Integer.MAX_VALUE - rst) < (str.charAt(i) - '0')){
				//System.out.println(Integer.MAX_VALUE);
				return Integer.MAX_VALUE;
			}
			if(minus== -1 && (Integer.MIN_VALUE - minus*rst) > ('0' - str.charAt(i) )){
				//System.out.println(Integer.MAX_VALUE);
				return Integer.MIN_VALUE;
			}
			rst += str.charAt(i) - '0';
			//System.out.println(rst);
		}
		
		
		return rst*minus;
    }

	public static void main(String[] args) {
		StringtoInteger sti = new StringtoInteger();
		System.out.print(sti.myAtoi("    +1146905820n1"));


	}

}
