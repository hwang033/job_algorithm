package leetcode;

public class BestTimetoBuyandSellStockII {
    public int maxProfit(int[] prices) {
    	int profit = 0;
    	int prev = Integer.MAX_VALUE;
    	for(int i: prices){
    		if (i > prev){
    			profit += (i-prev);
    		}
    		prev = i;
    	}
    	return profit;        
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
