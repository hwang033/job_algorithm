package leetcode;

public class ExcelSheetColumnNumber {
	
    public int titleToNumber(String s) {
    	int multipler = 1;
    	int value = 0;
    	int rst = 0;
    	for(int i = s.length() - 1; i >= 0; i--){
    		value = s.charAt(i) - 'A' + 1;
    		rst += value*multipler;
    		multipler *= 26;
    	}
        return rst;
    }
	public static void main(String[] args) {
		ExcelSheetColumnNumber esc = new ExcelSheetColumnNumber();
		System.out.print(esc.titleToNumber("AB"));

	}

}
