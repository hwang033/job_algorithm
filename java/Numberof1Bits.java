package leetcode;

public class Numberof1Bits {
    // you need to treat n as an unsigned value
    // this method can not handle 10000000000000000000000000000000
	public int hammingWeight(int n) {
        int rst = 0;
    	while(n > 0){
        	rst += (n&1);
        	n >>>= 1;
        }
    	return rst;
	}	
	//much better method
	public int hammingWeight2(int n) {
	     int c;
	     for (c = 0; n != 0; ++c)
	         n = n & (n - 1);
	     return c;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Numberof1Bits nob = new Numberof1Bits();
		int x;
		x = 2147483647;
		nob.hammingWeight(x);
		
		
	}

}
