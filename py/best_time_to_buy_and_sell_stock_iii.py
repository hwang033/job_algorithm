import pdb
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        #f1 calculate max profit from 1st to last one
        #f2 calculate max profit from last one to 1st
        if not prices:
            return 0
            
        f1 = [0 for x in xrange(len(prices))]
        f2 = [0 for x in xrange(len(prices))]
        
        minimum = prices[0]
        for idx, val in enumerate(prices):
            if val > minimum:
                f1[idx] = max(f1[idx-1], val - minimum)
            else:
                minimum = val
                f1[idx] = f1[idx-1]
        
        maximum = prices[-1]        
        for idx, val in enumerate(prices[::-1]):
            if val < maximum:
                f2[idx] = max(f2[idx-1], maximum - val)
            else:
                maximum = val
                f2[idx] = f2[idx-1]

        return max([f1[idx] + f2[len(prices)-idx-1] for\
                    idx in xrange(len(prices))])

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([2,1])
    print s.maxProfit([2,1,2,0,1])
