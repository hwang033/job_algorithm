package leetcode;

import java.util.Arrays;

public class LongestPalindromicSubstring {
    
	public String longestPalindrome(String s) {
		//dynamic programming O(n^2) time complexity, O(n) space complexity
		int[] opt_cur = new int[s.length()];
		int prev_j = 0;
		int prev_j_1 = 0;
		String rst = null;
		int maxLength = 0;
		for(int i=s.length()-1; i>=0; i--){
			for(int j=i; j<s.length(); j++){
				prev_j_1 = prev_j;
				prev_j = opt_cur[j];
				if(s.charAt(i)==s.charAt(j)){
					if(j - i <= 2){
						//aa, aba
						opt_cur[j] = j - i + 1;
					}
					else if(prev_j_1 != 0){
						// check if s.substring(i+1, j-1) is palindrome
						opt_cur[j] = prev_j_1 + 2;
					}
					else{
							
						opt_cur[j] = 0;
					}
					
					if(opt_cur[j] > maxLength){
						maxLength = opt_cur[j];
						rst = s.substring(i, j+1);
					}
					
				}
				else{
					opt_cur[j] = 0;
				}
			}//for j
			//System.out.println(Arrays.toString(opt_cur));
			prev_j_1 = 0;
			prev_j = opt_cur[0];
		}//for i
				
		return rst;        
    }

	public static void main(String[] args) {
	
		LongestPalindromicSubstring lps = new LongestPalindromicSubstring();
		System.out.print(lps.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"));	
	}

}
